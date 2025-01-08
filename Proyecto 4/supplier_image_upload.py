#!/usr/bin/env python3

# Importamos la librería requests para realizar la subida de imágenes.
import requests
import os

# URL del servidor donde se suben las imágenes.
url = "http://[external-IP-address]/upload/"
image_directory = "/ruta/a/supplier-data/images"

def upload_image(filename):
    """Sube la imagen al servidor usando una solicitud POST."""
    try:
        with open(os.path.join(image_directory, filename), 'rb') as opened_file:
            # Enviamos la imagen como archivo adjunto
            response = requests.post(url, files={'file': opened_file})
            print(f"Uploaded {filename}: {response.status_code}")  # Imprime el código de respuesta
    except Exception as e:
        # Si hay algún error, lo mostramos
        print(f"Error uploading {filename}: {e}")

if __name__ == "__main__":
    # Subimos todas las imágenes en formato .jpeg
    for image_file in os.listdir(image_directory):
        if image_file.endswith(".jpeg"):
            upload_image(image_file)