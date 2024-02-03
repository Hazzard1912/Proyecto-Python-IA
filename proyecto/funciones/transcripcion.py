import speech_recognition as sr
import os
import uuid

from pydub import AudioSegment

from funciones.consultar_openai import preparar_prompt
from funciones.guardar_respuesta import guardar_respuesta

directorio_resultados = "results"

if not os.path.exists(directorio_resultados):
    os.makedirs(directorio_resultados)

recognizer = sr.Recognizer()

def reconocer_discurso(audio_path):

    with sr.AudioFile(audio_path) as source:
        audio = recognizer.record(source)
    try:
        consulta = recognizer.recognize_google(audio, language="es-CO")
        respuesta = preparar_prompt(consulta)
        guardar_respuesta(respuesta, directorio_resultados)

    except sr.UnknownValueError:
        print("No se entendió el audio")
    except sr.RequestError as e:
        print("error; {0}".format(e))


def revisar_formato(audio_path):

    conversiones_dir = "conversiones"

    if not os.path.exists(conversiones_dir):
        os.makedirs(conversiones_dir)

    extension = audio_path.split(".")[-1]
    
    match extension:
        case "wav":
            reconocer_discurso(audio_path)
        case "mp3":
            audio_path = mp3_a_wav(audio_path, conversiones_dir)
            reconocer_discurso(audio_path)
        case "m4a":
            audio_path = m4a_a_wav(audio_path, conversiones_dir)
            reconocer_discurso(audio_path)
        case _:
            print("extension de archivo no soportada")

def mp3_a_wav(audio_path, output_folder):

      unique_filename = str(uuid.uuid4()) + ".wav"
      output_path = os.path.join(output_folder, unique_filename)

      try:

        audio = AudioSegment.from_mp3(audio_path)
        audio.export(output_path, format="wav")

        print(f"Conversión exitosa: {audio_path} a {output_path}")
        return output_path

      except Exception as e:

        print(f"Error al convertir {audio_path} a {output_path}: {str(e)}")

def m4a_a_wav(audio_path, output_folder):
    unique_filename = str(uuid.uuid4()) + ".wav"
    output_path = os.path.join(output_folder, unique_filename)

    try:

        audio = AudioSegment.from_file(audio_path, format="m4a")
        audio.export(output_path, format="wav")

        print(f"Conversión exitosa: {audio_path} a {output_path}")
        return output_path

    except Exception as e:
        print(f"Error al convertir {audio_path} a {output_path}: {str(e)}")