import sys
from PyQt6.QtCore import Qt, QAbstractListModel
            #Manejo de listas
class ModeloTarefas (QAbstractListModel):
            #Inicilizamos la clase y llamamos a la superclase
        def __init__(self, tarefas=None):
            super().__init__()
            #Se le asigna a tareas un valor o se crea como lista vacía
            self.tarefas = tarefas or []
            #definimos el metodo data
        def data (self, indice , rol):
            if rol ==Qt.ItemDataRole.DisplayRole:
            #igualamos una variable texto a la fila de la lista tarefas
                _, texo = self.tarefas [indice.row()]
                return texo
            #Devolvemos el tamaño de la lista
        def rowCount(self, indice):
            return  len(self.tarefas)



