import sqlite3
from clases.entities.Varietal import Varietal
from clases.entities.Vino import Vino


class VarietalDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def cargar_por_vino(self, vino: Vino):
        conn = self.conectar()
        cursor = conn.cursor()

        # Obtener todos los varietales asociados al vino desde la tabla intermedia
        cursor.execute('''
            SELECT var.id, var.descripcion 
            FROM Varietales var
            JOIN varietal_x_vino vxv ON var.id = vxv.varietal_id
            WHERE vxv.vino_id = ?
        ''', (vino.id,))

        rows = cursor.fetchall()
        conn.close()

        varietales = []
        for row in rows:
            varietal = Varietal(row[0], row[1])
            varietales.append(varietal)
            vino.varietales.append(varietal)

        return varietales
