import pandas as pd
import openpyxl  #Deben instalar esta biblioteca sino no funciona la generacion del archivo excel.
import os
from tkinter import ttk
import tkinter as tk


class PantallaExcel:
    def __init__(self, info_vinos, puntaje_vinos):
        self.info_vinos = info_vinos
        self.puntaje_vinos = puntaje_vinos
        self.confirmacion = None
        self.ventana = None
        self.generarExcel()

    def generarExcel(self):
        data = {'Nombre Vino': [], 'Precio Vino': [], 'Info Bodega': [], 'Ubicacion Bodega': [], 'Varietal': [],
                'Puntaje': []}
        for vino, puntaje in zip(self.info_vinos, self.puntaje_vinos):
            data['Nombre Vino'].append(vino[0])
            data['Precio Vino'].append(vino[1])
            data['Info Bodega'].append(str(vino[2][0]))
            data['Ubicacion Bodega'].append(str(vino[2][1]))
            data['Varietal'].append(vino[2][2])
            data['Puntaje'].append(puntaje)

        df = pd.DataFrame(data)
        df.to_excel('ranking_vinos.xlsx', index=False)

    def abrir_excel(self, pantalla):
        """
        Muestra una ventana de confirmación para abrir el archivo PDF generado.
        """
        # Crear una nueva ventana de confirmación
        self.ventana = pantalla.get_ventana()
        confirm_window = tk.Toplevel(self.ventana)
        confirm_window.title("Abrir Excel Generado")

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
        ttk.Label(frame, text="¿Desea abrir el excel generado?").grid(row=3, column=0, pady=5, sticky=tk.W)

        # Crear una variable para almacenar la confirmación del usuario
        self.confirmacion = tk.BooleanVar()

        # Crear botones de confirmar y cancelar
        button_frame = ttk.Frame(frame)
        button_frame.grid(row=4, column=0, pady=20)

        tk.Button(button_frame, text="Confirmar",
                  command=lambda: self.tomar_confirmacion_archivo(True, confirm_window),
                  bg='green', fg='white').grid(row=0, column=0, padx=10)
        tk.Button(button_frame, text="Cancelar",
                  command=lambda: self.tomar_confirmacion_archivo(False, confirm_window),
                  bg='red', fg='white').grid(row=0, column=1, padx=10)

    def tomar_confirmacion_archivo(self, confirmacion, window):

        """
        Toma la confirmación del usuario y abre el archivo PDF si se confirma.
        """
        window.destroy()
        ruta_excel = os.path.abspath("./ranking_vinos.xlsx")
        if confirmacion:
            # Verificar si el archivo existe
            if os.path.exists(ruta_excel):
                # Abrir el archivo PDF con el programa predeterminado del sistema
                os.startfile(ruta_excel)
            else:
                print("Operación cancelada.")
                return
        else:
            return
