import sqlite3
from DAO.BodegaDAO import BodegaDAO
from DAO.ResenaDAO import ResenaDAO
from DAO.VarietalDAO import VarietalDAO
from Entities.Vino import Vino


class VinoDAO:
    def __init__(self, db_path: str):
        self.db_path = db_path

    def conectar(self):
        return sqlite3.connect(self.db_path)

    def cargar_todos(self):
        conn = self.conectar()
        cursor = conn.cursor()

        cursor.execute('SELECT id, aniada, nombre, nota_de_cata, precio, id_bodega FROM vinos')
        rows = cursor.fetchall()
        conn.close()

        # Crear instancias de Vino con sus dependencias
        vinos = []
        for row in rows:
            # Primero, cargar la bodega asociada
            bodega = self.cargar_bodega(row[5])  # Cargar la bodega usando el bodega_id

            # Crear el objeto Vino
            vino = Vino(row[0], row[1], row[2], row[3], row[4], bodega)

            # Adjuntar las reseñas al vinos que corresponda
            self.cargar_resenas(vino)

            # hago lo mismo con los varietales
            self.cargar_varietales(vino)

            # Agregar el vino a la lista
            vinos.append(vino)

        return vinos

    def cargar_bodega(self, id_bodega: int):
        # Aquí, llamas al BodegaDAO para cargar la bodega relacionada
        bodega_dao = BodegaDAO(self.db_path)
        return bodega_dao.obtener_por_id(id_bodega)

    def cargar_resenas(self, vino: Vino):
        resena_dao = ResenaDAO(self.db_path)
        return resena_dao.cargar_resenias(vino)

    def cargar_varietales(self, vino: Vino):
        varietal_dao = VarietalDAO(self.db_path)
        return varietal_dao.cargar_por_vino(vino)
