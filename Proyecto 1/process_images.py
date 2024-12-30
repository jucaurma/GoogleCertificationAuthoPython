#!/usr/bin/env python3

from PIL import Image
import os

#Directorios
input_folder = "input_images"
output_folder = "output_images"

#Crear carpeta de salida si no existe
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

#Procesar cada imagen en la carpeta
for filename in os.listdir(input_folder):
    if filename.endswith((".png", ".jpg", ".jpeg")):  #Filtrar formatos válidos
        #Ruta completa de la imagen
        input_path = os.path.join(input_folder, filename)
        output_path = os.path.join(output_folder, filename)

        #Abrir la imagen
        with Image.open(input_path) as img:
            
            #Rotar la imagen 90 grados
            img = img.rotate(-90, expand = True)

            #Redimensionar la imagen (128x128 píxeles)
            img = img.resize((128,128))

            #Convertir a formato JPEG y guardar
            output_file = os.path.splitext(filename)[0] + ".jpeg"   #Cambiar extensión a .jpeg
            output_path = os.path.join(output_folder, output_file)
            img.convert("RGB").save(output_path, "JPEG")

        print(f"Procesado: {filename}")

print("Todas las imágenes han sido procesadas y guardadas en la carpeta de destino.")