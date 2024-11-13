import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
from PIL import Image, ImageTk
from datetime import datetime
import os


class PantallaRankingVinos:
    def __init__(self):
        self.confirmacion = None
        self.gestor = None
        self.fechaDesde = None
        self.fechaHasta = None
        self.habilitado = False
        self.ventana = tk.Tk()
        self.ventana.state("zoomed")  # Maximiza la ventana
        self.ventana.title("Ranking de Vinos")
        self.ventana.configure(bg="#4B1F1F")

        # Deshabilitar el cambio de tamaño de la ventana
        # self.ventana.resizable(False, False)

        # Configuración de estilos para los widgets de tkinter
        style = ttk.Style()
        style.theme_use("clam")  # Establece el tema de los widgets
        # Configura el estilo para los labels (etiquetas)
        style.configure("TLabel", background="#4B1F1F", foreground="#FFFFFF", font=("Helvetica", 14))
        # Configura el estilo para los botones
        style.configure("TButton", background="#F5E9DC", foreground="#FFFFFF", font=("Helvetica", 12), padding=10)
        # Configura el estilo para los campos de entrada (Entry)
        style.configure("TEntry", padding=5, font=("Helvetica", 12))
        # Configura el estilo para los frames (contenedores)
        style.configure("TFrame", background="#4B1F1F")

        # Creación de un label para el título
        self.label = ttk.Label(self.ventana, text="Ranking de Vinos", font=("Helvetica", 24, "bold"), foreground="#F5E9DC")
        self.label.pack(pady=20)
        # Coloca el label en la ventana

        # Creación de un frame para la fecha desde
        frame_fecha_desde = ttk.Frame(self.ventana)
        frame_fecha_desde.pack(pady=10, padx=20)  # Coloca el frame en la ventana

        # Creación de un label y un campo de entrada para la fecha desde
        label_fecha_desde = ttk.Label(frame_fecha_desde, text="•Fecha Desde(DD/MM/AAAA):")
        label_fecha_desde.grid(row=0, column=0, padx=(0, 10), sticky="e")  # Coloca el label en el frame
        self.entry_fecha_desde = ttk.Entry(frame_fecha_desde, width=20)
        self.entry_fecha_desde.grid(row=0, column=1, padx=10, sticky="ew")  # Coloca el campo de entrada en el frame

        # Creación de un botón con un icono de calendario para la fecha desde
        icono_calendario = Image.open("./resources/calendario.png")
        icono_calendario = icono_calendario.resize((20, 20), Image.Resampling.LANCZOS)

        self.icono_calendario = ImageTk.PhotoImage(icono_calendario)
        self.boton_calendario_desde = ttk.Button(frame_fecha_desde, image=self.icono_calendario,
                                                 command=lambda: self.abrirCalendario("desde"))
        self.boton_calendario_desde.grid(row=0, column=2, padx=10)  # Coloca el botón en el frame

        # Creación de un calendario para la fecha desde
        self.calendar_fecha_desde = Calendar(self.ventana, selectmode="day", date_pattern="dd/MM/yyyy")
        self.calendar_fecha_desde.bind("<<CalendarSelected>>",
                                       self.tomarSeleccionFechaDesde)  # Vincula el evento de selección del
        # calendario a la función correspondiente

        # Creación de un frame para la fecha hasta
        frame_fecha_hasta = ttk.Frame(self.ventana)
        frame_fecha_hasta.pack(pady=10, padx=20)

        # Creación de un label y un campo de entrada para la fecha hasta
        label_fecha_hasta = ttk.Label(frame_fecha_hasta, text="• Fecha Hasta(DD/MM/AAAA):")
        label_fecha_hasta.grid(row=0, column=0, padx=(0, 10), sticky="e")  # Coloca el label en el frame
        self.entry_fecha_hasta = ttk.Entry(frame_fecha_hasta, width=20)
        self.entry_fecha_hasta.grid(row=0, column=1, padx=10, sticky="ew")  # Coloca el campo de entrada en el frame

        # Creación de un botón con un icono de calendario para la fecha hasta
        self.boton_calendario_hasta = ttk.Button(frame_fecha_hasta, image=self.icono_calendario,
                                                 command=lambda: self.abrirCalendario("hasta"))
        self.boton_calendario_hasta.grid(row=0, column=2, padx=10)  # Coloca el botón en el frame

        # Creación de un calendario para la fecha hasta
        self.calendar_fecha_hasta = Calendar(self.ventana, selectmode="day", date_pattern="dd/MM/yyyy")
        self.calendar_fecha_hasta.bind("<<CalendarSelected>>",
                                       self.tomarSeleccionFechaHasta)  # Vincula el evento de selección del calendario
        # a la función correspondiente

        # Creación de label para mostrar el error
        self.label_error = ttk.Label(self.ventana, text="", foreground="red")
        self.label_error.pack()

        # Configuración de las columnas de los frames para que se expandan con la ventana
        frame_fecha_desde.columnconfigure(1, weight=1)
        frame_fecha_hasta.columnconfigure(1, weight=1)

        # Creación de un frame para el ListBox
        self.frame_listbox = ttk.Frame(self.ventana)
        self.frame_listbox.pack(pady=10, padx=20)  # Coloca el frame en la ventana

        # Creación de un label para el ListBox
        self.label_listbox = ttk.Label(self.frame_listbox, text="Seleccione el tipo de reportes:")
        self.label_listbox.pack(side=tk.LEFT, padx=10)  # Coloca el label en el frame

        # Creación del ListBox con los tipos de reportes
        self.tipoResena = ttk.Combobox(self.frame_listbox, values=[], state="readonly")
        self.tipoResena.pack(side=tk.LEFT, padx=10)

        # Creación de un label para el ListBox para Tipos Visualizacion
        self.label_listbox = ttk.Label(self.frame_listbox, text="Seleccione el tipo de visualizacion:")
        self.label_listbox.pack(side=tk.LEFT, padx=10)  # Coloca el label en el frame

        # Creación del ListBox con los tipos de reportes
        self.tipoVisualizacion = ttk.Combobox(self.frame_listbox, values=[], state="readonly")
        self.tipoVisualizacion.pack(side=tk.LEFT, padx=10)

        # Creación de botón para generar ranking
        self.boton_generar_ranking = ttk.Button(self.ventana, text="Generar Ranking", command=self.opcionGenerarRanking)
        self.boton_generar_ranking.pack(pady=20)  # Coloca el botón debajo de los combobox


    def abrirCalendario(self, fecha):
        self.ocultarCalendarios()
        boton = self.boton_calendario_desde if fecha == "desde" else self.boton_calendario_hasta
        x = boton.winfo_rootx() - self.ventana.winfo_rootx()
        y = boton.winfo_rooty() - self.ventana.winfo_rooty() + 30

        if fecha == "desde":
            self.calendar_fecha_desde.place(x=x, y=y)
            self.calendar_fecha_desde.lift()
        elif fecha == "hasta":
            self.calendar_fecha_hasta.place(x=x, y=y)
            self.calendar_fecha_hasta.lift()

    def ocultarCalendarios(self):
        self.calendar_fecha_desde.place_forget()
        self.calendar_fecha_hasta.place_forget()

    def opcionGenerarRanking(self):
        if self.ventana.winfo_exists() and self.habilitado:
            return self.gestor.opcionGenerarRankingVinos()
        self.habilitarVentana()
        return self.gestor.opcionGenerarRankingVinos()

    def habilitarVentana(self):
        self.habilitado = True
        return self.ventana.mainloop()

    def pedirSeleccionFechas(self):
        fechaDesde = self.tomarSeleccionFechaDesde()
        fechaHasta = self.tomarSeleccionFechaHasta()

        if not self.validarPeriodo(fechaDesde, fechaHasta):
            self.pedirSeleccionFechas()
        return self.gestor.tomarSeleccionFechaDesdeyHasta(fechaDesde, fechaHasta)

    def tomarSeleccionFechaDesde(self, event=None):
        fecha_str = self.calendar_fecha_desde.get_date()
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        self.entry_fecha_desde.delete(0, tk.END)
        self.entry_fecha_desde.insert(0, fecha.strftime("%d/%m/%Y"))
        self.fechaDesde = fecha
        self.ocultarCalendarios()
        return fecha

    def tomarSeleccionFechaHasta(self, event=None):
        fecha_str = self.calendar_fecha_hasta.get_date()
        fecha = datetime.strptime(fecha_str, "%d/%m/%Y")
        if self.fechaDesde:
            if not self.validarPeriodo(self.fechaDesde, fecha):
                self.label_error.config(text="La fecha hasta debe ser mayor que la fecha desde")
                return None
        self.label_error.config(text="")
        self.entry_fecha_hasta.delete(0, tk.END)
        self.entry_fecha_hasta.insert(0, fecha.strftime("%d/%m/%Y"))
        self.fechaHasta = fecha
        self.ocultarCalendarios()
        self.label_error.config(text="")
        return fecha

    def validarPeriodo(self, fechaDesde, fechaHasta):
        if fechaDesde >= fechaHasta:
            self.label_error.config(text="La fecha hasta debe ser mayor que la fecha desde")
            return False
        self.label_error.config(text="")
        self.mostrarListBoxTipoReportes()  # Muestra el listbox con los tipos de reportes
        return True

    def setGestor(self, gestor):
        self.gestor = gestor
        self.tipoResena['values'] = self.gestor.tipoReportes
        self.tipoResena.current(0)  # Selecciona el primer elemento de la lista
        self.tipoVisualizacion['values'] = self.gestor.tipoVisualizacion
        self.tipoVisualizacion.current(0)  # Selecciona el primer elemento de la lista

    def solicitarTipoResena(self):
        return self.tomarSeleccionTipoResena()

    def tomarSeleccionTipoResena(self):
        tipoResena = self.tipoResena.get()  # Corregido a get()
        return self.gestor.tomarSeleccionTipoResena(tipoResena)

    def solicitarFormatoDelReporte(self):
        return self.tomarFormatoDelReporte()

    def tomarFormatoDelReporte(self):
        tipoVisualizacion = self.tipoVisualizacion.get()  # Corregido a get()
        return self.gestor.tomarFormatoDelReporte(tipoVisualizacion)

    def mostrarListBoxTipoReportes(self):
        self.frame_listbox.pack(pady=10, padx=20)  # Coloca el frame en la ventana
        return

    def mostrarListBoxTiposVisualizacion(self):
        self.frame_listbox.pack(pady=10, padx=20)  # Coloca el frame en la ventana
        return

    def solicitarConfirmacionReporte(self):
        # Crear una nueva ventana
        confirm_window = tk.Toplevel(self.ventana)
        confirm_window.title("Confirmar selección")

        # Definir tamaño de ventana
        window_width = 400
        window_height = 300

        # Obtener tamaño de la pantalla
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()

        # Calcular posición
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Configurar geometría de la ventana
        confirm_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Crear un Frame para organizar los elementos
        frame = ttk.Frame(confirm_window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Mostrar las fechas seleccionadas, tipo de reseña y tipo de visualización
        ttk.Label(frame, text=f"Fecha Desde: {self.fechaDesde.strftime('%d/%m/%Y')}").grid(row=0, column=0, pady=5,
                                                                                           sticky=tk.W)
        ttk.Label(frame, text=f"Fecha Hasta: {self.fechaHasta.strftime('%d/%m/%Y')}").grid(row=1, column=0, pady=5,
                                                                                           sticky=tk.W)
        ttk.Label(frame, text=f"Tipo de Reseña: {self.tipoResena.get()}").grid(row=2, column=0, pady=5, sticky=tk.W)
        ttk.Label(frame, text=f"Tipo de Visualización: {self.tipoVisualizacion.get()}").grid(row=3, column=0, pady=5,
                                                                                             sticky=tk.W)

        # Crear una variable para almacenar la confirmación del usuario
        self.confirmacion = tk.BooleanVar()

        # Crear botones de confirmar y cancelar
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, pady=20)

        tk.Button(button_frame, text="Confirmar",
                  command=lambda: self.tomarConfirmacion(True, confirm_window),
                  bg='green', fg='white').grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Cancelar",
                  command=lambda: self.tomarConfirmacion(False, confirm_window),
                  bg='red', fg='white').grid(row=0, column=1, padx=10)

        # Esperar a que el usuario cierre la ventana de confirmación antes de retornar la confirmación
        self.ventana.wait_window(confirm_window)
        return self.confirmacion.get()

    def tomarConfirmacion(self, confirmacion, window):
        # Set the confirmation and close the confirmation window
        self.confirmacion.set(confirmacion)
        window.destroy()
        if confirmacion:
            self.gestor.tomarConfirmacionReporte(confirmacion)
        
    def getVentana(self):
        return self.ventana
    
    def abrirPDF(self):
        """
        Muestra una ventana de confirmación para abrir el archivo PDF generado.
        """
        # Crear una nueva ventana de confirmación
        confirm_window = tk.Toplevel(self.ventana)
        confirm_window.title("Abrir PDF Generado")

        # Definir tamaño de ventana
        window_width = 400
        window_height = 200

        # Obtener tamaño de la pantalla
        screen_width = self.ventana.winfo_screenwidth()
        screen_height = self.ventana.winfo_screenheight()

        # Calcular posición para centrar la ventana
        position_top = int(screen_height / 2 - window_height / 2)
        position_right = int(screen_width / 2 - window_width / 2)

        # Configurar geometría de la ventana
        confirm_window.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

        # Crear un Frame para organizar los elementos
        frame = ttk.Frame(confirm_window, padding="20")
        frame.pack(fill=tk.BOTH, expand=True)

        # Mostrar el mensaje de confirmación
        ttk.Label(frame, text="¿Desea abrir el PDF generado?").grid(row=3, column=0, pady=5, sticky=tk.W)

        # Crear una variable para almacenar la confirmación del usuario
        self.confirmacion = tk.BooleanVar()

        # Crear botones de confirmar y cancelar
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, pady=20)

        tk.Button(button_frame, text="Confirmar",
                  command=lambda: self.tomarConfirmacionArchivo(True, confirm_window),
                  bg='green', fg='white').grid(row=0, column=0, padx=10)

        tk.Button(button_frame, text="Cancelar",
                  command=lambda: self.tomarConfirmacionArchivo(False, confirm_window),
                  bg='red', fg='white').grid(row=0, column=1, padx=10)

        # Esperar a que el usuario cierre la ventana de confirmación antes de retornar la confirmación
        self.ventana.wait_window(confirm_window)
        return self.tomarConfirmacionArchivo

    def tomarConfirmacionArchivo(self, confirmacion, window):
        """
        Toma la confirmación del usuario y abre el archivo PDF si se confirma.
        """
        if window is not None:
            window.destroy()

        if confirmacion:
            # Obtener la ruta absoluta del archivo PDF
            ruta_pdf = os.path.abspath("./ranking_vinos.pdf")

            # Verificar si el archivo existe
            if os.path.exists(ruta_pdf):
                # Abrir el archivo PDF con el programa predeterminado del sistema
                os.startfile(ruta_pdf)
            else:
                print("El archivo PDF no existe.")
        else:
            print("Operación cancelada.")
        return
