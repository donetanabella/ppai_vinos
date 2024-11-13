import sqlite3
from datetime import datetime
from DAO.RegionVitivinicolaDAO import RegionVitivinicolaDAO
from Entities.Resena import Resena
from Entities.Vino import Vino


class ResenaDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def cargar_resenias(self, vino: Vino):
        conn = self.conectar()
        cursor = conn.cursor()

        # Obtener los datos de la reseña
        cursor.execute('SELECT id, comentario, es_premium, fecha, puntaje FROM resenas WHERE id_vino = ?', (vino.id,))
        row = cursor.fetchone()
        conn.close()

        valor_premium = False
        if row[2] == 1:
            valor_premium = True
        fecha_resenia = datetime.strptime(row[3], "%d-%m-%Y")

        # Crear y retornar el objeto Bodega
        return Resena(row[0], row[1], valor_premium, fecha_resenia, row[4], vino)
