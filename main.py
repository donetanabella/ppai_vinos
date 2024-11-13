import tkinter as tk
#Importamos Clases a usar
from clases.Bodega import Bodega
from clases.DAO.VinoDAO import VinoDAO
from clases.Pais import Pais
from clases.PantallaRankingVinos import PantallaRankingVinos
from clases.Varietal import Varietal
from clases.RegionVitivinicola import RegionVitivinicola
from clases.GestorRankingVinos import GestorRankingVinos
from clases.Provincia import Provincia
from clases.Vino import Vino
from clases.Resena import Resena
from datetime import datetime


def main():
     listaVinos = [
         Vino(añada=2005, imagenEtiqueta="https://example.com/etiqueta1.jpg", nombre="Vino 1",
              notaDeCataBodega="Notas de frutos rojos maduros", precioARS=3589.0,
              bodega=Bodega("Bodega 250", "Catena Zapata",
                            RegionVitivinicola("Valle de Uco", Provincia("Mendoza", Pais("Argentina")))),
              varietal=Varietal("Tempranillo"),
              resena=[
                  Resena("Robusto y equilibrado", datetime(2023, 3, 15), 9),
                  Resena("Ideal para carnes asadas", datetime(2022, 6, 22), 8)
              ]),
         Vino(añada=2018, imagenEtiqueta="https://example.com/etiqueta2.jpg", nombre="Vino 2",
              notaDeCataBodega="Aromas intensos a ciruelas", precioARS=2773.0,
              bodega=Bodega("Bodega 150", "Trapiche",
                            RegionVitivinicola("Valle de Uco", Provincia("Mendoza", Pais("Argentina")))),
              varietal=Varietal("Merlot"), resena=[
                 Resena("Aromas intensos", datetime(2022, 6, 10), 8),
                 Resena("Perfecto para quesos curados", datetime(2021, 8, 12), 9)
             ]),
         Vino(añada=2006, imagenEtiqueta="https://example.com/etiqueta3.jpg", nombre="Vino 3",
              notaDeCataBodega="Taninos maduros", precioARS=4382.0,
              bodega=Bodega("Bodega 20", "Bodegas Muga",
                            RegionVitivinicola("Rioja Alta", Provincia("La Rioja", Pais("España")))),
              varietal=Varietal("Cabernet Sauvignon"),
              resena=[
                  Resena("Complejo y elegante", datetime(2021, 9, 12), 9),
                  Resena("Frutas negras persistentes", datetime(2019, 11, 7), 8)
              ]),
         Vino(añada=2013, imagenEtiqueta="https://example.com/etiqueta4.jpg", nombre="Vino 4",
              notaDeCataBodega="Toques de rosas", precioARS=4807.0,
              bodega=Bodega("Bodega 10", "Domaine de la Romanée-Conti",
                            RegionVitivinicola("Côte de Nuits", Provincia("Borgoña", Pais("Francia")))),
              varietal=Varietal("Pinot Noir"),
              resena=[
                  Resena("Elegante y largo", datetime(2020, 11, 5), 10)
              ]),
         Vino(añada=2015, imagenEtiqueta="https://example.com/etiqueta5.jpg", nombre="Vino 5",
              notaDeCataBodega="Frutado y fresco", precioARS=3220.0,
              bodega=Bodega("Bodega 55", "Bodega Norton",
                            RegionVitivinicola("Luján de Cuyo", Provincia("Mendoza", Pais("Argentina")))),
              varietal=Varietal("Malbec"),
              resena=[
                  Resena("Notas de ciruela y tabaco", datetime(2023, 1, 8), 9),
                  Resena("Buen balance y estructura", datetime(2021, 5, 12), 8)
              ]),
         Vino(añada=2010, imagenEtiqueta="https://example.com/etiqueta6.jpg", nombre="Vino 6",
              notaDeCataBodega="Aromas a especias", precioARS=3940.0,
              bodega=Bodega("Bodega 3", "Viña San Pedro",
                            RegionVitivinicola("Valle Central", Provincia("Cauquenes", Pais("Chile")))),
              varietal=Varietal("Carmenere"),
              resena=[
                  Resena("Profundo y complejo", datetime(2022, 8, 2), 7),
                  Resena("Final suave y prolongado", datetime(2020, 7, 30), 9)
              ]),
         Vino(añada=2020, imagenEtiqueta="https://example.com/etiqueta7.jpg", nombre="Vino 7",
              notaDeCataBodega="Notas cítricas y minerales", precioARS=2170.0,
              bodega=Bodega("Bodega 88", "Marqués de Riscal",
                            RegionVitivinicola("Rueda", Provincia("Castilla y León", Pais("España")))),
              varietal=Varietal("Verdejo"),
              resena=[
                  Resena("Fresco y ligero", datetime(2023, 6, 20), 9)
              ]),
         Vino(añada=2008, imagenEtiqueta="https://example.com/etiqueta8.jpg", nombre="Vino 8",
              notaDeCataBodega="Aromas de café y tabaco", precioARS=4500.0,
              bodega=Bodega("Bodega 7", "Bodegas Emilio Moro",
                            RegionVitivinicola("Ribera del Duero", Provincia("Castilla y León", Pais("España")))),
              varietal=Varietal("Tinto Fino"),
              resena=[
                  Resena("Taninos finos y elegantes", datetime(2021, 10, 15), 9),
                  Resena("Excelente estructura", datetime(2019, 12, 12), 8)
              ]),
         Vino(añada=2014, imagenEtiqueta="https://example.com/etiqueta9.jpg", nombre="Vino 9",
              notaDeCataBodega="Fresco y afrutado", precioARS=3080.0,
              bodega=Bodega("Bodega 95", "Finca La Anita",
                            RegionVitivinicola("Alto Valle", Provincia("Neuquén", Pais("Argentina")))),
              varietal=Varietal("Bonarda"),
              resena=[
                  Resena("Perfecto para pastas", datetime(2022, 3, 15), 8)
              ]),
         Vino(añada=2016, imagenEtiqueta="https://example.com/etiqueta10.jpg", nombre="Vino 10",
              notaDeCataBodega="Notas de frutas tropicales", precioARS=2890.0,
              bodega=Bodega("Bodega 12", "Casa Silva",
                            RegionVitivinicola("Valle del Maule", Provincia("Maule", Pais("Chile")))),
              varietal=Varietal("Chardonnay"),
              resena=[
                  Resena("Toques cítricos", datetime(2021, 4, 8), 9)
              ]),
         Vino(añada=2017, imagenEtiqueta="https://example.com/etiqueta11.jpg", nombre="Vino 11",
              notaDeCataBodega="Aromas de frutos secos y un toque ahumado", precioARS=4600.0,
              bodega=Bodega("Bodega 300", "Bodega Garzón",
                            RegionVitivinicola("Maldonado", Provincia("Maldonado", Pais("Uruguay")))),
              varietal=Varietal("Tannat"),
              resena=[
                  Resena("Taninos firmes con buena estructura", datetime(2022, 7, 15), 8),
                  Resena("Perfecto para carnes a la parrilla", datetime(2021, 11, 20), 9)
              ]),
         Vino(añada=2012, imagenEtiqueta="https://example.com/etiqueta12.jpg", nombre="Vino 12",
              notaDeCataBodega="Notas a especias dulces y frutos negros", precioARS=5120.0,
              bodega=Bodega("Bodega 210", "Santa Rita",
                            RegionVitivinicola("Valle del Maipo", Provincia("Santiago", Pais("Chile")))),
              varietal=Varietal("Syrah"),
              resena=[
                  Resena("Elegante y sedoso en boca", datetime(2020, 3, 5), 9),
                  Resena("Intenso con un final largo", datetime(2019, 6, 25), 10)
              ]),
         Vino(añada=2019, imagenEtiqueta="https://example.com/etiqueta13.jpg", nombre="Vino 13",
              notaDeCataBodega="Fresco con notas cítricas y florales", precioARS=2350.0,
              bodega=Bodega("Bodega 350", "Domaine William Fèvre",
                            RegionVitivinicola("Chablis", Provincia("Borgoña", Pais("Francia")))),
              varietal=Varietal("Chardonnay"),
              resena=[
                  Resena("Muy fresco, ideal para mariscos", datetime(2023, 2, 12), 9)
              ]),
         Vino(añada=2021, imagenEtiqueta="https://example.com/etiqueta14.jpg", nombre="Vino 14",
              notaDeCataBodega="Aromas a frutas de hueso y toques minerales", precioARS=2780.0,
              bodega=Bodega("Bodega 450", "Zuccardi",
                            RegionVitivinicola("Valle de Paraje Altamira", Provincia("Mendoza", Pais("Argentina")))),
              varietal=Varietal("Sauvignon Blanc"),
              resena=[
                  Resena("Fresco, ligero y bien equilibrado", datetime(2023, 4, 7), 8),
                  Resena("Excelente acidez y notas tropicales", datetime(2022, 10, 15), 9),
                  Resena("Perfecto para platos de pescado", datetime(2021, 8, 1), 7)
              ]),
         Vino(añada=2009, imagenEtiqueta="https://example.com/etiqueta15.jpg", nombre="Vino 15",
              notaDeCataBodega="Complejo con toques de chocolate amargo y frutos secos", precioARS=3920.0,
              bodega=Bodega("Bodega 510", "Penfolds",
                            RegionVitivinicola("Barossa Valley", Provincia("Australia Meridional", Pais("Australia")))),
              varietal=Varietal("Shiraz"),
              resena=[
                  Resena("Gran cuerpo con un final largo y especiado", datetime(2022, 11, 30), 10),
                  Resena("Aromas intensos a frutos negros", datetime(2021, 1, 20), 8)
              ])
     ]
     # debo tener las listas de datos
     vino_dao = VinoDAO('vinos.db')
     listaVinos = vino_dao.cargar_todos()

     # Creamos un Gestor y una panatalla y los seteaamos mutuamente
     gestor = GestorRankingVinos()
     pantalla = PantallaRankingVinos()

     gestor.setVinos(listaVinos)

     # Seteamos el gestor y la pantalla mutuamente
     gestor.setPantalla(pantalla)
     pantalla.setGestor(gestor)

     # Inicializamos la pantalla
     pantalla.opcionGenerarRanking()



if __name__ == "__main__":
    main()
