from Pantallas.PantallaExcel import PantallaExcel
from fpdf import FPDF
from Interfaces.InterfazAgregado import InterfazAgregado
from Interfaces.IteradorVinos import *

# sisi el modelo de analisis lo tiene como atributo del gestor


class GestorRankingVinos(InterfazAgregado):
    def __init__(self):
        # Atributos de la clase
        self.confirmacion = None
        self.pantalla = None  # Objeto de la clase Pantalla
        self.lista_vinos = None  # Lista de objetos de la clase Vino
        self.fecha_desde = None  # DateTime
        self.fecha_hasta = None  # DateTime
        self.info_vinos = []
        self.info_vinos_ordenados = None
        self.puntaje_vinos = []
        self.tipo_reportes = ["Premium", "Normales", "Amigos"]
        self.tipo_reporte_seleccionado = None
        self.tipo_visualizacion = ["PDF", "Excel"]
        self.puntaje_vinos = []
        self.pantalla_excel = None

    def habilitar_ranking(self):
        print("Habilitando ranking...")

    def opcion_generar_ranking_vinos(self):
        # Se solicita el periodo para el ranking
        return self.pantalla.pedir_seleccion_fechas()

    def obtener_informacion_vino_y_resenia_en_periodo(self):
        # for vino in self.listaVinos:
        #    if vino.tenesResenaEnPeriodo(self.fechaDesde, self.fechaHasta):
        #        nombreVino = vino.getNombre()
        #        precioVino = vino.getPrecio()
        #        infoBodega = vino.buscarInfoBodega()
        #        if [nombreVino, precioVino,
        #            infoBodega] not in self.infoVinos:  # Check if the wine info is not already in the list
        #            self.infoVinos.append([nombreVino, precioVino, infoBodega])
        # return self.calcularPromedioResenasEnPeriodo()
        filtros = [self.fecha_desde, self.fecha_hasta, self.tipo_reportes]
        iterador = self.crear_iterador(self.lista_vinos, filtros)
        iterador.primero()
        while not iterador.ha_terminado():
            vinos = iterador.actual()
            self.info_vinos.append(vinos)
            iterador.siguiente()
        return self.calcular_promedio_resenias_en_periodo()

    def crear_iterador(self, elementos: List[object], filtros: List[object]):
        return IteradorVinos(elementos, filtros)

    def set_pantalla(self, pantalla):
        self.pantalla = pantalla

    def set_vinos(self, lista_vinos):
        self.lista_vinos = lista_vinos

    def tomar_seleccion_fecha_desde_y_hasta(self, fecha_desde, fecha_hasta):
        self.fecha_hasta = fecha_hasta
        self.fecha_desde = fecha_desde
        return self.pantalla.solicitar_tipo_resenia()

    def tomar_seleccion_tipo_resenia(self, tipo_reporte):
        self.tipo_reporte_seleccionado = tipo_reporte
        return self.pantalla.solicitar_formato_del_reporte()

    def tomar_formato_del_reporte(self, tipo_visualizacion):
        self.tipo_visualizacion = tipo_visualizacion
        return self.pantalla.solicitar_confirmacion_reporte()

    def set_tipo_reportes(self, tipos):
        self.tipo_reportes = tipos

    def tomar_confirmacion_reporte(self, confirmacion):
        self.confirmacion = confirmacion
        return self.obtener_informacion_vino_y_resenia_en_periodo()

    def set_tipo_visualizacion(self, tipo_visualizacion):
        self.tipo_visualizacion = tipo_visualizacion

    def calcular_promedio_resenias_en_periodo(self):
        for vino in self.lista_vinos:
            puntaje = vino.calcular_puntaje_resenia_en_periodo(self.fecha_desde, self.fecha_hasta)
            self.puntaje_vinos.append(puntaje)
        return self.ordenar_vinos_segun_promedio_puntaje()

    def ordenar_vinos_segun_promedio_puntaje(self):
        # Ordenamos usando solo los puntajes para evitar el error de comparación
        self.info_vinos_ordenados = [x for _, x in
                                     sorted(zip(self.puntaje_vinos, self.info_vinos), key=lambda pair: pair[0],
                                            reverse=True)]
        self.puntaje_vinos.sort(reverse=True)

        if self.tipo_visualizacion == "PDF":
            return self.generar_archivo_PDF(self.info_vinos_ordenados, self.puntaje_vinos)
        return self.generar_archivo_excel(self.info_vinos_ordenados, self.puntaje_vinos)

    def generar_archivo_excel(self, info_vinos, puntaje_vinos):
        self.pantalla_excel = PantallaExcel(info_vinos, puntaje_vinos)
        return self.fin_CU()

    def fin_CU(self):
        if self.tipo_visualizacion == "PDF":
            return self.pantalla.abrir_PDF()
        elif self.tipo_visualizacion == "Excel":
            return self.pantalla_excel.abrir_excel(self.pantalla)
        return

    def generar_archivo_PDF(self, info_vinos, puntaje_vinos):
        print(info_vinos)
        contador = 0
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        # Encabezado
        pdf.cell(200, 10, txt="Ranking de Vinos", ln=True, align='C')

        # Tabla de vinos
        pdf.ln(10)
        pdf.set_font("Arial", size=10)
        pdf.cell(30, 10, txt="Nombre", border=1)
        pdf.cell(15, 10, txt="Precio", border=1)
        pdf.cell(53, 10, txt="Info Bodega", border=1)
        pdf.cell(45, 10, txt="Ubicacion Bodega", border=1)
        pdf.cell(41, 10, txt="Varietal", border=1)
        pdf.cell(14, 10, txt="Puntaje", border=1)
        pdf.ln(10)

        for vino in info_vinos[:10]:

            print(vino)

            # Usar los métodos getters para acceder a los atributos
            nombre_bodega, ubicacion_bodega, descripcion_varietal = vino.buscar_info_bodega()

            pdf.cell(30, 10, txt=vino.get_nombre(), border=1)
            pdf.cell(15, 10, txt=str(vino.get_precio()), border=1)
            pdf.cell(53, 10, txt=' ' + str(nombre_bodega), border=1)
            pdf.cell(45, 10, txt=' ' + str(ubicacion_bodega), border=1)
            pdf.cell(41, 10, txt=' ' + str(descripcion_varietal), border=1)
            pdf.cell(14, 10, txt=str(puntaje_vinos[contador]), border=1)
            pdf.ln(10)
            contador += 1

        # Guardar archivo PDF
        pdf.output("ranking_vinos.pdf", "F")
        print("Archivo PDF creado exitosamente.")
        return self.fin_CU()
