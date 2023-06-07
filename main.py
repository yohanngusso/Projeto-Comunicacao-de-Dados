import sys
import numpy as np
import matplotlib.pyplot as plt
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()

        # Configuração da janela principal
        self.setWindowTitle("Codificação NRZ")
        self.setGeometry(200, 200, 1000, 700)

        # Criação dos widgets
        self.lbl_mensagem = QLabel("Mensagem:")
        self.txt_mensagem = QLineEdit()
        self.btn_codificar = QPushButton("Codificar")
        self.lbl_mensagem_codificada = QLabel("Mensagem Codificada:")
        self.lbl_mensagem_binaria = QLabel("Mensagem Binária:")
        self.lbl_grafico = QLabel("Gráfico:")
        self.canvas = FigureCanvas(Figure(figsize=(5, 3)))
        self.layout = QVBoxLayout()
        self.layout.addWidget(self.lbl_mensagem)
        self.layout.addWidget(self.txt_mensagem)
        self.layout.addWidget(self.btn_codificar)
        self.layout.addWidget(self.lbl_mensagem_codificada)
        self.layout.addWidget(self.lbl_mensagem_binaria)
        self.layout.addWidget(self.lbl_grafico)
        self.layout.addWidget(self.canvas)
        self.setLayout(self.layout)

        # Conexão do botão com a função de codificação
        self.btn_codificar.clicked.connect(self.codificar_mensagem)

    def codificar_mensagem(self):
        # Obtenção da mensagem inserida pelo usuário
        mensagem = self.txt_mensagem.text()

        # Codificação NRZ
        codificacao_nrz = []
        for i in range(len(mensagem)):
            if mensagem[i] == '0':
                codificacao_nrz.append(-1)
            else:
                codificacao_nrz.append(1)

        # Conversão para binário
        mensagem_binaria = ''.join(format(ord(i), '08b') for i in mensagem)

        # Atualização das labels da interface gráfica
        self.lbl_mensagem_codificada.setText(f"Mensagem Codificada: {codificacao_nrz}")
        self.lbl_mensagem_binaria.setText(f"Mensagem Binária: {mensagem_binaria}")

        # Plotagem do gráfico
        fig = Figure()
        ax = fig.add_subplot(111)
        ax.plot(np.arange(len(codificacao_nrz)), codificacao_nrz)
        ax.set_title("Codificação NRZ")
        ax.set_xlabel("Tempo")
        ax.set_ylabel("Nível de Tensão")
        self.canvas.figure = fig
        self.canvas.draw()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
