import sqlite3
from app.domain.entidades import Tarea
from app.domain.repositorio import RepositorioTareas

class RepositorioTareaSQLite(RepositorioTareas):
    def __init__(self, db_file):
        self.conn = sqlite3.connect(db_file)
        self.crear_tabla()

    def crear_tabla(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS tareas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                descripcion TEXT,
                completa BOOLEAN NOT NULL CHECK (completa IN (0, 1))  -- Asegura que solo se acepten 0 o 1
            )
        ''')
        self.conn.commit()

    def obtener_tareas(self):
        cursor = self.conn.cursor()
        cursor.execute("SELECT id, titulo, descripcion, completa FROM tareas")
        rows = cursor.fetchall()
        return [Tarea(id=row[0], titulo=row[1], descripcion=row[2], completa=bool(row[3])) for row in rows]

    def agregar_tarea(self, tarea: Tarea):
        # Asegurar que completa es un booleano (0 o 1)
        completa_value = 1 if tarea.completa else 0
        cursor = self.conn.cursor()
        cursor.execute("INSERT INTO tareas (titulo, descripcion, completa) VALUES (?, ?, ?)", 
                       (tarea.titulo, tarea.descripcion, completa_value))
        self.conn.commit()

    def marcar_completada(self, tarea_id: int, completa: bool):
        # Asegurar que completa es un booleano (0 o 1)
        completa_value = 1 if completa else 0
        cursor = self.conn.cursor()
        cursor.execute("UPDATE tareas SET completa = ? WHERE id = ?", (completa_value, tarea_id))
        self.conn.commit()

    def eliminar_tarea(self, tarea_id: int):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM tareas WHERE id = ?", (tarea_id,))
        self.conn.commit()
