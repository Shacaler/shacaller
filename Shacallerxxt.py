import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QHBoxLayout, QLabel, QCheckBox, QGridLayout


class ControleEstoque(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Controle de Estoque e Vendas')

        # Botão de estoque
        self.btn_estoque = QPushButton('Estoque')
        self.btn_estoque.clicked.connect(self.show_estoque)

        # Botão de vendas
        self.btn_vendas = QPushButton('Vendas')
        self.btn_vendas.clicked.connect(self.show_vendas)

        # Botão de cancelamento
        self.btn_cancelamento = QPushButton('Cancelamento')
        self.btn_cancelamento.clicked.connect(self.show_cancelamento)

        # Layout principal
        layout = QVBoxLayout()
        layout.addWidget(self.btn_estoque)
        layout.addWidget(self.btn_vendas)
        layout.addWidget(self.btn_cancelamento)
        self.setLayout(layout)

    def show_estoque(self):
        # Código para exibir a tela de estoque
        self.estoque = QWidget()
        self.estoque.setWindowTitle('Estoque')

        # Layout principal
        estoque_layout = QVBoxLayout()

        # Layout de copos
        copos_layout = QVBoxLayout()
        copos_label = QLabel('Copos:')
        copos_layout.addWidget(copos_label)

        copos = {
            'Copo de 250ML': 10,
            'Copo de 330ML': 20,
            'Copo de 440ML': 15,
            'Copo de 550ML': 12,
            'Copo de 700ML': 8
        }

        for copo, quantidade in copos.items():
            copo_layout = QHBoxLayout()
            copo_label = QLabel(copo)
            copo_layout.addWidget(copo_label)

            copo_qtd_label = QLabel(f'Quantidade: {quantidade}')
            copo_layout.addWidget(copo_qtd_label)

            # Botão de adicionar copo
            copo_add_button = QPushButton('+')
            copo_add_button.clicked.connect(lambda _, q=quantidade, l=copo_qtd_label, n=copo: self.add_item(q, l, n))
            copo_layout.addWidget(copo_add_button)

            # Botão de subtrair copo
            copo_sub_button = QPushButton('-')
            copo_sub_button.clicked.connect(lambda _, q=quantidade, l=copo_qtd_label, n=copo: self.sub_item(q, l, n))
            copo_layout.addWidget(copo_sub_button)

            copos_layout.addLayout(copo_layout)

        estoque_layout.addLayout(copos_layout)

        # Layout de potes
        potes_layout = QVBoxLayout()
        potes_label = QLabel('Potes:')
        potes_layout.addWidget(potes_label)

        potes = {
            'Pote de 250ML': 5,
            'Pote de 380ML': 7,
            'Pote de 530ML': 10,
            'Pote de 750ML': 8,
            'Pote de 1 LITRO': 4
        }

        for pote, quantidade in potes.items():
            pote_layout = QHBoxLayout()
            pote_label = QLabel(pote)
            pote_layout.addWidget(pote_label)

            pote_qtd_label = QLabel(f'Quantidade: {quantidade}')
            pote_layout.addWidget(pote_qtd_label)

            # Botão de adicionar pote
            pote_add_button = QPushButton('+')
            pote_add_button.clicked.connect(lambda: self.add_item(self.pote_quantidade, self.pote_numero))

        # Botão de remover pote
            pote_remove_button = QPushButton('-')
            pote_remove_button.clicked.connect(lambda: self.remove_item(self.pote_quantidade, self.pote_numero))

        # Adiciona widgets ao layout de potes
            potes_layout.addWidget(pote_label)
            potes_layout.addWidget(pote_add_button)
            potes_layout.addWidget(self.pote_quantidade)
            potes_layout.addWidget(pote_remove_button)
            potes_layout.addWidget(self.pote_numero)

        # Adiciona layout de copos e layout de potes ao layout principal de estoque
        estoque_layout.addLayout(copos_layout)
        estoque_layout.addLayout(potes_layout)

        self.estoque.setLayout(estoque_layout)

    def add_item(self, quantidade_label, numero_label):
        # Adiciona 1 à quantidade
        quantidade = int(quantidade_label.text())
        quantidade += 1
        quantidade_label.setText(str(quantidade))

        # Atualiza o número de adição
        numero = int(numero_label.text())
        numero += 1
        numero_label.setText(str(numero))

    def remove_item(self, quantidade_label, numero_label):
        # Verifica se a quantidade atual é maior que 0
        quantidade = int(quantidade_label.text())
        if quantidade > 0:
            # Subtrai 1 da quantidade
            quantidade -= 1
            quantidade_label.setText(str(quantidade))

            # Atualiza o número de subtração
            numero = int(numero_label.text())
            numero -= 1
            numero_label.setText(str(numero))
            #Botão para adicionar Potes
           # Botão de subtrair pote
            pote_sub_button = QPushButton('-')
            pote_sub_button.clicked.connect(lambda: subtrai_item(pote_numero_label))
            pote_layout.addWidget(pote_sub_button)

            # Número de adição e subtração de potes
            pote_numero_label = QLabel('0')
            pote_layout.addWidget(pote_numero_label)

            # Adiciona o layout de potes ao layout principal
            estoque_layout.addLayout(copos_layout)
            estoque_layout.addLayout(potes_layout)

            self.estoque.setLayout(estoque_layout)

        def add_item(label):
            numero = int(label.text())
            numero += 1
            label.setText(str(numero))

        def subtrai_item(label):
            numero = int(label.text())
            numero -= 1
            label.setText(str(numero))
            
        def show_estoque(self):
            # Código para exibir a tela de estoque
            self.estoque = QWidget()
            self.estoque.setWindowTitle('Estoque')

            # Layout principal
            estoque_layout = QVBoxLayout()

            # Layout de copos
            copos_layout = QVBoxLayout()
            copos_layout.addWidget(QLabel('Copos'))

            # Botão de adicionar copo
            copo_add_button = QPushButton('+')
            copo_add_button.clicked.connect(lambda: add_item(copo_numero_label))
            copos_layout.addWidget(copo_add_button)

            # Número de adição e subtração de copos
            copo_numero_label = QLabel('0')
            copos_layout.addWidget(copo_numero_label)

            # Botão de subtrair copo
            copo_sub_button = QPushButton('-')
            copo_sub_button.clicked.connect(lambda: subtrai_item(copo_numero_label))
            copos_layout.addWidget(copo_sub_button)

            # Layout de potes
            potes_layout = QVBoxLayout()
            potes_layout.addWidget(QLabel('Potes'))

            # Botão de adicionar pote
            pote_add_button = QPushButton('+')
            pote_add_button.clicked.connect(lambda: add_item(pote_numero_label))
            potes_layout.addWidget(pote_add_button)

            # Número de adição e subtração de potes
            pote_numero_label = QLabel('0')
            potes_layout.addWidget(pote_numero_label)

            # Botão de subtrair pote
            pote_sub_button = QPushButton('-')
            pote_sub_button.clicked.connect(lambda: subtrai_item(pote_numero_label))
            potes_layout.addWidget(pote_sub_button)

            # Adiciona o layout de copos e de potes ao layout principal
            estoque_layout.addLayout(copos_layout)
            estoque_layout.addLayout(potes_layout)

            self.estoque.setLayout(estoque_layout)
            self.estoque.show()

        def show_vendas(self):
            # Código para exibir a tela de vendas
            pass

        def show_cancelamento(self):
            # Código para exibir a tela de cancelamento
            pass

    if __name__ == '__main__':
        app = QApplication(sys.argv)
        controle_estoque = ControleEstoque()
        controle_estoque.show()
        sys.exit(app.exec_())
