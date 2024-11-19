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

        self.lstTarefas = QListView()
        self.lstTarefas.setModel(self.modelo)
        #Habilitamos una selección múltiple
        self.lstTarefas.setSelectionMode(QListView.SelectionMode.MultiSelection)
        caixav.addWidget(self.lstTarefas)
        #Boton borrar tareaa
        caixaHBotons= QHBoxLayout()
        btnBorrar = QPushButton("Borrar")
        btnBorrar.pressed.connect (self.on_btnBorrar_pressed)
        #Boton tarea echa
        btnFeito = QPushButton ("Feito")
        btnFeito.pressed.connect (self.on_btnFeito_pressed)
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

    def on_btnFeito_pressed(self):
        indices = self.lstTarefas.selectedIndexes()
        if indices:
            for indice in indices:
                #Cogemos el indice y el texto
                _, texto = self.modelo.tarefas [indice.row()]
                #Cambiamos el indice a True para que aparezca el icono
                self.modelo.tarefas [indice.row()] = (True,texto)
            self.modelo.dataChanged.emit(indice,indice)
            self.lstTarefas.clearSelection()


    def on_btnBorrar_pressed(self):
        indices = self.lstTarefas.selectedIndexes()
        if indices:
            # Invertimos los índices y eliminamos desde el final para evitar problemas de reindexación
            for indice in sorted(indices, reverse=True):
                print(indice.row())
                del self.modelo.tarefas[indice.row()]
            # Permitimos que se actualicen las tareas con esta línea
            self.modelo.layoutChanged.emit()
            # Borramos la selección anterior para actualizar los índices
            self.lstTarefas.clearSelection()



if __name__ == "__main__":
        aplicacion = QApplication(sys.argv)
        fiestra = ExampleQListView()
        aplicacion.exec()



