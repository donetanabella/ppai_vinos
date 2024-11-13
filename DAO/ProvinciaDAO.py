import sqlite3
from DAO.PaisDAO import PaisDAO
from Entities.Provincia import Provincia



class ProvinciaDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def obtener_por_id(self, provincia_id: int):
        conn = self.conectar()
        cursor = conn.cursor()

        # Obtener la provincia y el país asociado
        cursor.execute('SELECT id, nombre, id_pais FROM provincias WHERE id = ?', (provincia_id,))
        row = cursor.fetchone()
        conn.close()

        # Cargar el país asociado
        pais = self.cargar_pais(row[2])

        # Crear y retornar el objeto Provincia
        return Provincia(row[0], row[1], pais)

    def cargar_pais(self, pais_id: int):
        # Llamar al PaisDAO para obtener el país
        pais_dao = PaisDAO(self.db_path)
        return pais_dao.obtener_por_id(pais_id)
