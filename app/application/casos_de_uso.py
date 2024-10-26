from app.domain.entidades import Tarea
from app.domain.repositorio import RepositorioTareas

class GestionTareas:
    def __init__(self, repositorio: RepositorioTareas):
        self.repositorio = repositorio

    def obtener_tareas(self):
        return self.repositorio.obtener_tareas()

    def agregar_tarea(self, tarea: Tarea):
        self.repositorio.agregar_tarea(tarea)

    def marcar_completada(self, tarea_id: int, completa: bool):
        self.repositorio.marcar_completada(tarea_id, completa)

    def eliminar_tarea(self, tarea_id: int):
        self.repositorio.eliminar_tarea(tarea_id)
