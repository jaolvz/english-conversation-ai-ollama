from english_AI import EnglishAI


ai = EnglishAI()
def processar_comando(comando, ai):

    if comando.lower() == '/exit':
        print('AI: Goodbye!')
        return False

    if comando.lower() == '/reset':
        ai.reset()
        print('AI: Conversation reset.')
        return 'reset'


    if comando == '/help':
        print(
            'Comandos disponíveis:\n'
            '  /help  - mostrar os comandos\n'
            '  /reset - resetar a conversa\n'
            '  /exit  - fechar o programa'
        )
        return 'help'

    return None


ai = EnglishAI()


while True:

    mensagem = input('You: ')

    comando = processar_comando(mensagem, ai)

    if comando == 'exit':
        break

    if comando in ('reset','help'):
        continue

    resposta = ai.chat(mensagem)

    print('AI:', resposta)