import sys
from PySide6.QtCore import Qt, QThread, Signal
from english_AI import EnglishAI 
from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QTextEdit,
    QLineEdit,
    QPushButton,
    QVBoxLayout,
    QHBoxLayout
)

class Worker(QThread):

    resposta_pronta = Signal(object)

    def __init__(self, ai, mensagem):
        super().__init__()

        self.ai = ai
        self.mensagem = mensagem

    def run(self):
        resposta = self.ai.chat(self.mensagem)
        self.resposta_pronta.emit(resposta)

app = QApplication(sys.argv)
ai = EnglishAI()

janela = QWidget()
janela.setWindowTitle("English AI Tutor")
janela.setFixedSize(300, 550)
janela.setStyleSheet("background-color: white;")


titulo = QLabel("English AI Tutor")
titulo.setAlignment(Qt.AlignCenter)
titulo.setStyleSheet("font-size: 20px; ; font-family: Arial;")

conversa = QTextEdit()
conversa.setReadOnly(True)
conversa.setStyleSheet("""
    QTextEdit {
        border: 1px solid black;
        border-radius: 10px;
        padding: 10px;
        background-color: white;
    }

    QScrollBar:vertical {
        width: 6px;
        background: transparent;
        margin: 5px 2px 5px 0px;
    }

    QScrollBar::handle:vertical {
        background: #999999;
        border-radius: 3px;
        min-height: 30px;
    }

    QScrollBar::handle:vertical:hover {
        background: #666666;
    }

    QScrollBar::add-line:vertical,
    QScrollBar::sub-line:vertical {
        height: 0px;
    }

    QScrollBar::add-page:vertical,
    QScrollBar::sub-page:vertical {
        background: transparent;
    }
""")

entrada = QLineEdit()
entrada.setPlaceholderText("Digite sua mensagem...")
entrada.setStyleSheet("""
    border-radius: 10px;
    border: 1px solid black;
    padding:10px;
    background-color: white;
""")



botao_enviar = QPushButton("Enviar")
botao_enviar.setStyleSheet("""
    border-radius: 10px;
    border: 1px solid black;
    padding:10px;
    background-color: white;
""")
def finalizar_resposta(resposta):

    correction = resposta["correction"]
    explanation = resposta["explanation"]
    reply = resposta["reply"]

    cursor = conversa.textCursor()
    cursor.movePosition(cursor.MoveOperation.End)
    cursor.select(cursor.SelectionType.BlockUnderCursor)
    cursor.removeSelectedText()

    mensagem_original = worker.mensagem

    if correction.strip().lower() == mensagem_original.strip().lower():

        conversa.append(
            f'<b>AI:</b><br>'
            f'{reply}'
        )

    else:

        conversa.append(
            f'<b>AI:</b><br>'
            f'<span style="color:red;"><b>Correction:</b> {correction}</span><br><br>'
            f'<span style="color:green;"><b>Explanation:</b> {explanation}</span><br><br>'
            f'{reply}'
        )

    entrada.setEnabled(True)
    botao_enviar.setEnabled(True)
    entrada.setFocus()
def enviar_mensagem():

    mensagem = entrada.text()

    if not mensagem.strip():
        return

    conversa.append(f"<b>You:</b> {mensagem}")

    entrada.clear()

    entrada.setEnabled(False)
    botao_enviar.setEnabled(False)

    conversa.append("<i>AI is typing...</i>")

    global worker

    worker = Worker(ai, mensagem)

    worker.resposta_pronta.connect(finalizar_resposta)

    worker.start()

botao_enviar.clicked.connect(enviar_mensagem)
entrada.returnPressed.connect(enviar_mensagem)



layout_entrada = QHBoxLayout()
layout_entrada.addWidget(entrada)
layout_entrada.addWidget(botao_enviar)



layout_principal = QVBoxLayout()
layout_principal.addWidget(titulo)
layout_principal.addWidget(conversa)
layout_principal.addLayout(layout_entrada)


janela.setLayout(layout_principal)



def fechar_programa(event):
    ai.reset()
    event.accept()

janela.closeEvent = fechar_programa
janela.show()
sys.exit(app.exec())


