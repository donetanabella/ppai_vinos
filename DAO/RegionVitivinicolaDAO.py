import sqlite3

from clases.DAO.ProvinciaDAO import ProvinciaDAO
from clases.entities.RegionVitivinicola import RegionVitivinicola


class RegionVitivinicolaDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def obtener_por_id(self, region_id: int):
        conn = self.conectar()
        cursor = conn.cursor()

        # Obtener la región y su provincia asociada
        cursor.execute('SELECT id, nombre, id_provincia FROM regiones_vitivinicolas WHERE id = ?', (region_id,))
        row = cursor.fetchone()
        conn.close()

        # Cargar la provincia asociada
        provincia = self.cargar_provincia(row[2])

        # Crear y retornar el objeto RegionVitivinicola
        return RegionVitivinicola(row[0], row[1], provincia)

    def cargar_provincia(self, provincia_id: int):
        # Llamar al ProvinciaDAO para obtener la provincia asociada
        provincia_dao = ProvinciaDAO(self.db_path)
        return provincia_dao.obtener_por_id(provincia_id)
