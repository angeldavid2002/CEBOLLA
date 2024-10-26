from abc import ABC, abstractmethod
from .entidades import Tarea

class RepositorioTareas(ABC):
    @abstractmethod
    def obtener_tareas(self):
        pass

    @abstractmethod
    def agregar_tarea(self, tarea: Tarea):
        pass

    @abstractmethod
    def marcar_completada(self, tarea_id: int, completa: bool):
        pass

    @abstractmethod
    def eliminar_tarea(self, tarea_id: int):
        pass
