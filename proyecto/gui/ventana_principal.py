import os
import shutil

import tkinter as tk
from tkinter import filedialog
from funciones.transcripcion import revisar_formato

archivo = None

try:
    shutil.rmtree("conversiones")
    print("Carpeta eliminada con éxito")
except OSError as e:
    if e.errno == 2:
        pass
    else:
        print(f"Error al eliminar la carpeta: {str(e)}")

# Funciones de los botones:
def iniciar_proceso():
    global archivo
    if archivo:
        archivo_path = archivo.name
        revisar_formato(archivo_path)
    else:
        print("Por favor cargue un archivo")


def seleccionar_archivo():
    global archivo
    archivo = filedialog.askopenfile(
        filetypes=[("Archivos de audio", "*.mp3 *.wav *.m4a")]
    )
    if archivo:
        print(f"Archivo seleccionado: {archivo}")


# Especificaciones de la ventana:
ventana = tk.Tk()
ventana.title("Ayuda IA Redacción de Informes")
ventana.resizable(False, False)
ventana.geometry("300x200")

# Contenido de la ventana:
boton_seleccionar = tk.Button(
    ventana, text="Seleccionar Archivo de Audio", command=seleccionar_archivo
)
boton_seleccionar.pack(pady=10)

boton_iniciar = tk.Button(ventana, text="Iniciar Proceso", command=iniciar_proceso)
boton_iniciar.pack()

ventana.mainloop()
