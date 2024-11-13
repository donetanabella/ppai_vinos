import sqlite3

from clases.DAO.RegionVitivinicolaDAO import RegionVitivinicolaDAO
from clases.entities.Bodega import Bodega


class BodegaDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def obtener_por_id(self, bodega_id: int):
        conn = self.conectar()
        cursor = conn.cursor()

        # Obtener la bodega y su región asociada
        cursor.execute('SELECT id, nombre, descripcion, id_region FROM bodegas WHERE id = ?', (bodega_id,))
        row = cursor.fetchone()
        conn.close()

        # Cargar la región asociada a la bodega
        region = self.cargar_region(row[3])

        # Crear y retornar el objeto Bodega
        return Bodega(row[0], row[1], row[2], region)

    def cargar_region(self, region_id: int):
        # Llamar al RegionVitivinicolaDAO para obtener la región asociada
        region_dao = RegionVitivinicolaDAO(self.db_path)
        return region_dao.obtener_por_id(region_id)
