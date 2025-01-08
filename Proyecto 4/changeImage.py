#!/usr/bin/env python3

# Importamos la librería Pillow para manipular las imágenes.
from PIL import Image
import os

# Directorio de entrada y salida de las imágenes procesadas.
input_directory = "/ruta/a/supplier-data/images"
output_directory = "/ruta/a/supplier-data/images"

def process_image(filename):
    """Convierte las imágenes TIFF a JPEG y ajusta la resolución."""
    try:
        # Abrimos la imagen
        img = Image.open(os.path.join(input_directory, filename))
        img = img.convert("RGB")  # Convertir RGBA a RGB
        img = img.resize((600, 400))  # Ajustamos el tamaño de la imagen
        new_filename = filename.replace(".tiff", ".jpeg")  # Nombre de archivo nuevo
        img.save(os.path.join(output_directory, new_filename), "JPEG")  # Guardamos la imagen
        print(f"Processed {filename}")  # Imprime el nombre de la imagen procesada
    except Exception as e:
        # Si hay algún error, lo mostramos
        print(f"Error processing {filename}: {e}")

if __name__ == "__main__":
    # Procesamos todas las imágenes en el directorio que terminan en .tiff
    for file in os.listdir(input_directory):
        if file.endswith(".tiff"):
            process_image(file)