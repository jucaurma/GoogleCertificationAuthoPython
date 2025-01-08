# **Automatización de Actualización del Catálogo de Información**

## **Descripción del Proyecto**

Este proyecto tiene como objetivo automatizar el proceso de actualización del catálogo de productos de una tienda de frutas en línea utilizando datos proporcionados por los proveedores. La automatización incluye la conversión de imágenes, el procesamiento de descripciones, la carga de datos en un servidor web y la generación de reportes en PDF. Además, se implementa un sistema de monitoreo para garantizar la salud del sistema y enviar alertas en caso de fallos.

---

## **Funcionalidades**

1. **Procesamiento de Imágenes**  
   - Conversión de imágenes de formato `.TIFF` a `.JPEG`.
   - Reducción de la resolución de las imágenes de 3000x2000 a 600x400 píxeles.

2. **Carga de Imágenes**  
   - Subida de las imágenes procesadas al servidor web de la tienda de frutas.

3. **Procesamiento de Descripciones**  
   - Extracción de datos de los archivos `.txt` proporcionados por el proveedor.
   - Creación de objetos JSON que contienen nombre, peso, descripción y nombre de imagen.

4. **Carga de Datos al Servidor**  
   - Envío de las descripciones procesadas al servidor Django mediante solicitudes POST.

5. **Generación de Reportes en PDF**  
   - Creación de un informe PDF con el nombre y peso total de las frutas procesadas.

6. **Envío de Correos Electrónicos**  
   - Envío de un correo electrónico con el reporte en PDF al proveedor.

7. **Monitoreo del Sistema**  
   - Verificación periódica de:
     - Uso de CPU (> 80%).
     - Espacio disponible en disco (< 20%).
     - Memoria disponible (< 100MB).
     - Resolución del nombre del host `localhost`.
   - Envío de alertas por correo electrónico en caso de fallos.

---

## **Estructura del Proyecto**

project-directory/
│
├── supplier-data/                    # Directorio con datos del proveedor
│   ├── images/                       # Imágenes de frutas
│   ├── descriptions/                 # Archivos de descripción de frutas
│
├── changeImage.py                    # Script para procesar imágenes
├── supplier_image_upload.py          # Script para subir imágenes al servidor
├── run.py                            # Script para procesar descripciones y subirlas al servidor
├── reports.py                        # Script para generar informes en PDF
├── report_email.py                   # Script para enviar correos electrónicos con informes
├── health_check.py                   # Script para monitorear la salud del sistema
├── emails.py                         # Script para generar y enviar correos electrónicos
│
└── README.md                         # Archivo de documentación del proyecto

---

## **Requisitos**

- Python 3.x
- Librerías: `Pillow`, `requests`, `reportlab`, `psutil`
- Servidor Django configurado para la tienda de frutas.
- Acceso a un servidor SMTP para envío de correos electrónicos.

