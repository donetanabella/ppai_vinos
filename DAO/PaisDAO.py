import sqlite3
from Entities.Pais import Pais


class PaisDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def obtener_por_id(self, id_pais: int):
        conn = self.conectar()
        cursor = conn.cursor()

        # Obtener la provincia y el país asociado
        cursor.execute('SELECT id, nombre FROM paises WHERE id = ?', (id_pais,))
        row = cursor.fetchone()
        conn.close()

        # Crear y retornar el objeto Provincia
        return Pais(row[0], row[1])
