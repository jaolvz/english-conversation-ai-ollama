import ollama
import logging
from ollama import ResponseError
from config import MODEL , SYSTEM_PROMPT, MAX_HISTORY, MAX_MESSAGE_LENGTH, MEMORY_FILE
import json



logging.basicConfig(
    filename='logs/english_ai.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)


class EnglishAI:
    def __init__(self):
        self.model = MODEL
        self.mensagens = [
    {
        'role': 'system',
        'content': SYSTEM_PROMPT
    }
]
        self.carregar_memoria()



    def salvar_memoria(self):
        try:

            dados = {
                'messages': self.mensagens[1:]
            }

            with open(MEMORY_FILE, 'w', encoding='utf-8') as arquivo:
                json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        except Exception as erro:

            logging.error(f'Erro ao salvar memória: {erro}')

    def carregar_memoria(self):
        try:
            with open(MEMORY_FILE,'r', encoding='utf-8') as arquivo:
                dados = json.load(arquivo)
            self.mensagens = [
                            {
                                'role': 'system',
                                'content': SYSTEM_PROMPT
                            }
                        ] + dados['messages']

        except FileNotFoundError:
            logging.error('Arquivo de memória não encontrado.')

        except (json.JSONDecodeError, KeyError):
            logging.error('Arquivo de memória inválido')


    def _enviar_para_ollama(self,mensagens):
       
        try:

            resposta = ollama.chat(
                model=self.model,
                messages=mensagens
            )

            return resposta ['message']['content']

        except ResponseError as erro:
            logging.error(f'Erro do Ollama:{erro}')

            return None
        

        except Exception as erro:

            logging.error(f'Erro ao conectar com o Ollama: {erro}')

            return None
    def limitar_historico(self):

        max_mensagens = MAX_HISTORY*2

        if len(self.mensagens)> max_mensagens + 1:
            self.mensagens =[
                self.mensagens[0]
            ] + self.mensagens[-max_mensagens:]
        #pegando o system prompt e as 10 ultimas mensagems. concatenando como listas
    def reset(self):
        self.mensagens=[{
            'role':'system',
            'content':SYSTEM_PROMPT
        }]
        self.salvar_memoria()
    def validar_mensagem(self, mensagem):

        if not mensagem.strip():
            return 'A mensagem não pode estar vazia.'

        if len(mensagem) > MAX_MESSAGE_LENGTH:
            return f'A mensagem não pode ter mais de {MAX_MESSAGE_LENGTH} caracteres.'

        return None
    def chat(self,mensagem):

        erro= self.validar_mensagem(mensagem)

        if erro:
            return erro


        mensagens = self.mensagens + [{
            'role':'user',
            'content': mensagem
        }
        ]

        texto = self._enviar_para_ollama(mensagens)

        if texto is None:
            return 'Não foi possivel obter uma resposta do Ollama'
        

        self.mensagens.append( {
            'role':'user',
            'content':mensagem
        })



        self.mensagens.append({
            'role':'assistant',
            'content': texto
        })


        
        self.limitar_historico()

        self.salvar_memoria()

        return texto