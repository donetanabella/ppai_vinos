import tkinter as tk
# Importamos Clases a usar
from DAO.VinoDAO import VinoDAO
from Pantallas.PantallaRankingVinos import PantallaRankingVinos
from Gestores.GestorRankingVinos import GestorRankingVinos
from utilities.Clearer import Clearer


def main():
    Clearer.limpiar_todas_las_instancias()
    # debo tener las listas de datos
    vino_dao = VinoDAO('vinos.db')
    lista_vinos = vino_dao.cargar_todos()

    # Creamos un Gestor y una panatalla y los seteaamos mutuamente
    gestor = GestorRankingVinos()
    pantalla = PantallaRankingVinos()

    gestor.set_vinos(lista_vinos)

    # Seteamos el gestor y la pantalla mutuamente
    gestor.set_pantalla(pantalla)
    pantalla.set_gestor(gestor)

    # Inicializamos la pantalla
    pantalla.opcion_generar_ranking()


if __name__ == "__main__":
    main()
