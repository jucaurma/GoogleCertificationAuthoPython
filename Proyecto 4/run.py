#!/usr/bin/env python3

# Importamos las librerías necesarias
import os
import requests

# Directorio de las descripciones de frutas.
input_directory = "/ruta/a/supplier-data/descriptions"
# URL del servidor donde se suben los datos de las frutas.
url = "http://[external-IP-address]/fruits/"

def process_description(filename):
    """Procesa un archivo de descripción y lo sube al servidor en formato JSON."""
    with open(os.path.join(input_directory, filename), 'r') as file:
        # Leemos el archivo y extraemos los datos
        data = file.readlines()
        name = data[0].strip()
        weight = int(data[1].strip().replace("lbs", ""))
        description = data[2].strip()
        image_name = filename.replace(".txt", ".jpeg")
        
        # Creamos el payload con los datos extraídos
        payload = {
            "name": name,
            "weight": weight,
            "description": description,
            "image_name": image_name
        }
        
        # Enviamos el JSON al servidor
        response = requests.post(url, json=payload)
        print(f"Uploaded {name}: {response.status_code}")  # Imprime el código de respuesta

if __name__ == "__main__":
    # Procesamos todos los archivos de texto en el directorio de descripciones
    for file in os.listdir(input_directory):
        if file.endswith(".txt"):
            process_description(file)