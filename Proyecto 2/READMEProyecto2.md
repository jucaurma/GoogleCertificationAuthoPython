# Proyecto 2 - Procesamiento de Archivos de Texto y Carga en un Servidor Web

## Introducción

Este proyecto es parte de una certificación en automatización con Python, donde el objetivo era procesar reseñas de clientes almacenadas en archivos de texto y cargarlas en un servidor web para que se mostraran en el sitio web de la empresa.

El entorno del laboratorio proporcionaba un servidor web (configurado con Django) y archivos `.txt` con las reseñas de los clientes. Todo el trabajo debía realizarse en un entorno temporal y cerrado, con direcciones IP locales que no son accesibles fuera del laboratorio.

---

## Planteamiento del problema

Trabajas en una empresa que vende coches de segunda mano. La empresa recoge opiniones en forma de reseñas de clientes y las guarda en archivos de texto. El jefe solicita que estas reseñas sean procesadas y cargadas en la página web de la empresa.

El objetivo del proyecto es escribir un script en Python que:
1. Lea los archivos de texto en un directorio específico.
2. Procese su contenido y lo convierta en un formato adecuado (diccionarios de Python).
3. Cargue las reseñas en un servidor web mediante solicitudes HTTP (usando el método `POST`).

---

## Solución Propuesta

### **1. Planteamiento técnico**
Para resolver este problema, se desarrolló un script en Python con la siguiente estructura:
1. **Listar archivos**: Usar el módulo `os` para recorrer el directorio de archivos de texto.
2. **Leer y procesar contenido**: Abrir cada archivo y extraer las líneas correspondientes al título, nombre, fecha y comentario.
3. **Enviar datos al servidor**: Usar el módulo `requests` para realizar solicitudes HTTP `POST` al endpoint `/feedback/` del servidor.

### **2. Código del proyecto**

El script "run.py" que implementa la solución es el siguiente:

```python
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