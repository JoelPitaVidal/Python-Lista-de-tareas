import sys
from operator import contains
from os import lstat

from PyQt6.QtWidgets import QMainWindow, QVBoxLayout, QListView, QHBoxLayout, QPushButton, QLineEdit, QWidget, \
    QApplication

from ejemploMartes19 import ModeloTarefas


class ExampleQListView (QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Exemplo QlistView")
        listaTarefas = [(False, "Ir o ximnasio"),(False,"Facer a compra")]
        self.modelo = ModeloTarefas (listaTarefas)

        caixav = QVBoxLayout ()

        self.lstTArefas = QListView()
        self.lstTArefas.setModel(self.modelo)
        #Habilitamos una selección múltiple
        self.lstTArefas.setSelectionMode(QListView.SelectionMode.MultiSelection)
        caixav.addWidget(self.lstTArefas)
        #Boton borrar tareaa
        caixaHBotons= QHBoxLayout()
        btnBorrar = QPushButton("Borrar")
        btnBorrar.pressed.connect (self.on_btnBorrar_pressed)
        #Boton tarea echa
        btnFeito = QPushButton ("Feito")
        #btnFeito.pressed.connect (self.on_btnFeito_pressed)
        caixaHBotons.addWidget(btnBorrar)
        caixaHBotons.addWidget(btnFeito)

        caixav.addLayout(caixaHBotons)
        self.txtTarefa = QLineEdit ()
        #Boton añadir Tarea
        caixav.addWidget(self.txtTarefa)
        btnEngadirTarefa = QPushButton("Engadir Tarefa")
        btnEngadirTarefa.pressed.connect (self.on_btnEngadirTarefa_pressed)
        caixav.addWidget(btnEngadirTarefa)
        #Creamos el contenedor
        container = QWidget()
        container.setLayout(caixav)
        self.setCentralWidget(container)
        self.setFixedSize (400,300)
        self.show()

        #Boton añadir nueva tarea
    def on_btnEngadirTarefa_pressed(self):
        texto=self.txtTarefa.text().strip()
        if texto:
            #Añadimos nueva tarea sin hacer
            self.modelo.tarefas.append((False,texto))
            #Permitimos que se actualicen las tareas con esta linea
            self.modelo.layoutChanged.emit()
            self.txtTarefa.clear()

    def on_btnBorrar_pressed(self):
        indices = self.lstTArefas.selectedIndexes()
        if indices:
            # Invertimos los índices y eliminamos desde el final para evitar problemas de reindexación
            for indices in sorted(indices, key=lambda x: x.row(), reverse=True):
                del self.modelo.tarefas[indices.row()]
            # Permitimos que se actualicen las tareas con esta línea
            self.modelo.layoutChanged.emit()



if __name__ == "__main__":
        aplicacion = QApplication(sys.argv)
        fiestra = ExampleQListView()
        aplicacion.exec()



