import sys

from PyQt6.QtGui import QPalette, QColor
from PyQt6.QtWidgets import (QMainWindow, QApplication, QVBoxLayout, QWidget,QStackedLayout)

from CajaColor import CajaColor
from DatosFormulario import DatosWidget
from BotonesFormulario import Botones
from Botones_colores import boton_color
from RadioButtons import BotonRadio
from CheckButtos import ChechButton

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Ejemplo QStackLayout')
        self.setFixedSize(600, 600)
        paleta = self.palette()
        paleta.setColor(QPalette.ColorRole.Window, QColor("aquaMarine"))
        self.setPalette(paleta)

        caja_central = QVBoxLayout()
        caja_formulario = QVBoxLayout()

        datos_widget = DatosWidget()
        botones_widget = Botones()
        boton_color_cambio = boton_color()

        boton_color_cambio_radio = BotonRadio()

        self.boton_color_cambio_check = ChechButton()

        boton_color_cambio.button_cambio_rojo.clicked.connect(self.cambioRojo)
        boton_color_cambio.button_cambio_azul.clicked.connect(self.cambioAzul)
        boton_color_cambio.button_cambio_naranja.clicked.connect(self.cambioNaranja)
        boton_color_cambio.button_cambio_amarillo.clicked.connect(self.cambioAmarillo)
        boton_color_cambio.button_cambio_rosa.clicked.connect(self.cambioRosa)
        boton_color_cambio.button_cambio_gris.clicked.connect(self.cambioGris)
        boton_color_cambio.button_cambio_blanco.clicked.connect(self.cambioBlanco)
        boton_color_cambio.button_formulario.clicked.connect(self.cambioForm)

        caja_formulario.addLayout(datos_widget)
        caja_formulario.addLayout(botones_widget)

        boton_color_cambio_radio.button_cambio_rojo.clicked.connect(self.cambioRojo)
        boton_color_cambio_radio.button_cambio_rojo.setChecked(True) #Metodo para hacer que un boton esté presionando en el momento de iniciar la aplicación
        boton_color_cambio_radio.button_cambio_azul.clicked.connect(self.cambioAzul)
        boton_color_cambio_radio.button_cambio_naranja.clicked.connect(self.cambioNaranja)
        boton_color_cambio_radio.button_cambio_amarillo.clicked.connect(self.cambioAmarillo)
        boton_color_cambio_radio.button_cambio_rosa.clicked.connect(self.cambioRosa)
        boton_color_cambio_radio.button_cambio_gris.clicked.connect(self.cambioGris)
        boton_color_cambio_radio.button_cambio_blanco.clicked.connect(self.cambioBlanco)
        boton_color_cambio_radio.button_formulario.clicked.connect(self.cambioForm)

        self.boton_color_cambio_check.button_cambio_rojo.clicked.connect(self.setColoresCheck)
        self.boton_color_cambio_check.button_cambio_rojo.setChecked(True)  # Metodo para hacer que un boton esté presionando en el momento de iniciar la aplicación
        self.boton_color_cambio_check.button_cambio_azul.clicked.connect(self.setColoresCheck)
        self.boton_color_cambio_check.button_cambio_naranja.clicked.connect(self.setColoresCheck)
        self.boton_color_cambio_check.button_cambio_amarillo.clicked.connect(self.setColoresCheck)
        self.boton_color_cambio_check.button_cambio_rosa.clicked.connect(self.setColoresCheck)
        self.boton_color_cambio_check.button_cambio_gris.clicked.connect(self.setColoresCheck)
        self.boton_color_cambio_check.button_cambio_blanco.clicked.connect(self.setColoresCheck)
        self.boton_color_cambio_check.button_formulario.clicked.connect(self.setColoresCheck)

        self.stack_layout = QStackedLayout()
        self.stack_layout.addWidget(CajaColor("red"))
        self.stack_layout.addWidget(CajaColor("blue"))
        self.stack_layout.addWidget(CajaColor("orange"))
        self.stack_layout.addWidget(CajaColor("yellow"))
        self.stack_layout.addWidget(CajaColor("pink"))
        self.stack_layout.addWidget(CajaColor("gray"))
        self.stack_layout.addWidget(CajaColor("white"))
        container_formulario = QWidget()

        container_formulario.setLayout(caja_formulario)
        self.stack_layout.addWidget(container_formulario)

        caja_central.addLayout(self.stack_layout)
        caja_central.addLayout(boton_color_cambio)
        caja_central.addLayout(boton_color_cambio_radio)
        caja_central.addLayout(self.boton_color_cambio_check)

        self.stack_layout.setCurrentIndex(0)

        container = QWidget()
        container.setLayout(caja_central)
        self.setCentralWidget(container)
        self.show()

    def cambioRojo(self):
        self.stack_layout.setCurrentIndex(0)

    def cambioAzul(self):
        self.stack_layout.setCurrentIndex(1)

    def cambioNaranja(self):
        self.stack_layout.setCurrentIndex(2)

    def cambioAmarillo(self):
        self.stack_layout.setCurrentIndex(3)

    def cambioRosa(self):
        self.stack_layout.setCurrentIndex(4)

    def cambioGris(self):
        self.stack_layout.setCurrentIndex(5)

    def cambioBlanco(self):
        self.stack_layout.setCurrentIndex(6)

    def cambioForm(self):
        self.stack_layout.setCurrentIndex(7)

    def setColoresCheck(self):
        if self.boton_color_cambio_check.button_cambio_rojo.isChecked():
            self.stack_layout.setCurrentIndex(0)
        elif self.boton_color_cambio_check.button_cambio_azul.isChecked():
            self.stack_layout.setCurrentIndex(1)
        elif self.boton_color_cambio_check.button_cambio_naranja.isChecked():
            self.stack_layout.setCurrentIndex(2)
        elif self.boton_color_cambio_check.button_cambio_amarillo.isChecked():
            self.stack_layout.setCurrentIndex(3)
        elif self.boton_color_cambio_check.button_cambio_rosa.isChecked():
            self.stack_layout.setCurrentIndex(4)
        elif self.boton_color_cambio_check.button_cambio_gris.isChecked():
            self.stack_layout.setCurrentIndex(5)
        elif self.boton_color_cambio_check.button_cambio_blanco.isChecked():
            self.stack_layout.setCurrentIndex(6)
        elif self.boton_color_cambio_check.button_formulario.isChecked():
            self.stack_layout.setCurrentIndex(7)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    app.exec()