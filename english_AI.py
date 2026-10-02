import json
import logging
from groq import Groq
from config import (
    GROQ_API_KEY,
    MODEL,
    SYSTEM_PROMPT,
    MAX_HISTORY,
    MAX_MESSAGE_LENGTH,
    MEMORY_FILE
)


class EnglishAI:

    def __init__(self):

        self.client = Groq(api_key=GROQ_API_KEY)

        self.model = MODEL

        self.mensagens = []

        self.carregar_memoria()

    def salvar_memoria(self):

        try:

            with open(MEMORY_FILE, "w", encoding="utf-8") as arquivo:
                json.dump(
                    self.mensagens,
                    arquivo,
                    ensure_ascii=False,
                    indent=4
                )

        except Exception as erro:

            logging.error(
                f"Erro ao salvar memória: {erro}"
            )

    def carregar_memoria(self):

        try:

            with open(MEMORY_FILE, "r", encoding="utf-8") as arquivo:

                self.mensagens = json.load(arquivo)

        except FileNotFoundError:

            self.mensagens = []

        except (json.JSONDecodeError, OSError) as erro:

            logging.error(
                f"Arquivo de memória inválido: {erro}"
            )

            self.mensagens = []

    def limitar_historico(self):

        limite = MAX_HISTORY * 2

        if len(self.mensagens) > limite:

            self.mensagens = self.mensagens[-limite:]

    def reset(self):

        self.mensagens = []

        self.salvar_memoria()

    def validar_mensagem(self, mensagem):

        if not mensagem.strip():

            return False

        if len(mensagem) > MAX_MESSAGE_LENGTH:

            return False

        return True

    def chat(self, mensagem):

        if not self.validar_mensagem(mensagem):

            return {
                "correction": mensagem,
                "explanation": "Mensagem inválida.",
                "reply": "Could you try again?"
            }

        self.mensagens.append({
            "role": "user",
            "content": mensagem
        })

        mensagens_groq = [
            {
                "role": "system",
                "content": SYSTEM_PROMPT
            }
        ]

        for item in self.mensagens:

            mensagens_groq.append({
                "role": item["role"],
                "content": item["content"]
            })

        try:

            resposta = self.client.chat.completions.create(

                model=self.model,

                messages=mensagens_groq,

                temperature=0.7,

                response_format={
                    "type": "json_schema",
                    "json_schema": {
                        "name": "english_tutor_response",
                        "schema": {
                            "type": "object",
                            "properties": {
                                "correction": {
                                    "type": "string"
                                },
                                "explanation": {
                                    "type": "string"
                                },
                                "reply": {
                                    "type": "string"
                                }
                            },
                            "required": [
                                "correction",
                                "explanation",
                                "reply"
                            ],
                            "additionalProperties": False
                        }
                    }
                }
            )

            conteudo = resposta.choices[0].message.content

            resultado = json.loads(conteudo)

            self.mensagens.append({
                "role": "assistant",
                "content": conteudo
            })

            self.limitar_historico()

            self.salvar_memoria()

            return resultado

        except Exception as erro:

            logging.error(
                f"Erro ao conectar com o Groq: {erro}"
            )

            # Remove a última mensagem do usuário
            # caso a API tenha falhado.

            if self.mensagens and self.mensagens[-1]["role"] == "user":

                self.mensagens.pop()

            return {
                "correction": mensagem,
                "explanation": "Não foi possível obter uma resposta do Groq.",
                "reply": "Could you try again?"
            }