import random
import openai
import json
import os

dir = os.path.dirname(__file__)

config_file_path = os.path.join(dir, "config.json")

with open(config_file_path) as config_file:
    config = json.load(config_file)


OPENAI_API_KEY = config["OPENAI_API_KEY"]

openai.api_key = OPENAI_API_KEY

temperatura = random.uniform(0.5,0.8)

def preparar_prompt(consulta):

     global temperatura

     completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {
                "role": "system",
                "content": "Eres un inspector de riegos impecable, cuyo rol es, entre otros, redactar informes acerca de inspecciones a empresas. Te daré un reporte y me proveeras de la informacion redactada de una mejor manera y que se note profesional y pulida.",
            },
            {
                "role": "user",
                "content": f"{consulta}",
            },
        ],
        temperature=temperatura
    )
     respuesta = completion['choices'][0]['message']['content']
     return respuesta
