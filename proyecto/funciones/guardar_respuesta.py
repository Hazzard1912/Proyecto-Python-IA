import uuid
import os

def guardar_respuesta(respuesta, directorio):
    nombre_archivo = str(uuid.uuid4()) + ".txt"
    
    ruta_completa = os.path.join(directorio, nombre_archivo)
    
    with open(ruta_completa, "w") as archivo:
        archivo.write(respuesta)