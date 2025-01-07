#! /usr/bin/env python3

import os
import requests

# Ruta del directorio con los archivos de feedback
BASEPATH = '/data/feedback/'

# URL del endpoint (IP temporal proporcionada por el laboratorio)
SERVER_URL = 'http://127.0.0.1:80/feedback/'  # Este servidor solo estaba disponible en el laboratorio

# Obtener la lista de archivos en el directorio
files = os.listdir(BASEPATH)

# Procesar cada archivo de texto y almacenar los datos
for file in files:
    filepath = os.path.join(BASEPATH, file)
    with open(filepath, 'r') as f:
        # Crear un diccionario con el contenido del archivo
        data = {
            "title": f.readline().strip(),
            "name": f.readline().strip(),
            "date": f.readline().strip(),
            "feedback": f.read().strip()
        }
        # Realizar la solicitud POST al servidor
        response = requests.post(SERVER_URL, json=data)
        if response.status_code == 201:
            print(f"Uploaded feedback from {file}")
        else:
            print(f"Failed to upload {file}: {response.status_code}")