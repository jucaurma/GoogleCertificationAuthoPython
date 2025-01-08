# Proyecto 3: Generación automática de informes en PDF y envío por correo electrónico

Este proyecto forma parte de un laboratorio de automatización que tiene como objetivo procesar y resumir información, generar un informe en formato PDF y enviarlo automáticamente por correo electrónico a los destinatarios correspondientes.

## Descripción general

El proyecto simula un caso práctico en el que trabajas para una empresa que vende coches de segunda mano. Cada mes, es necesario enviar un resumen de las ventas realizadas a la dirección de la empresa. Este resumen se obtiene desde un servicio web, se procesa en Python, y se convierte en un informe profesional en formato PDF. Finalmente, el informe se envía por correo electrónico.

## Funcionalidades principales

1. **Procesamiento de datos:**
   - Recuperar información sobre las ventas desde un servicio web.
   - Resumir y organizar los datos en categorías relevantes (marcas, modelos, cantidades, ingresos totales, etc.).

2. **Generación de informes en PDF:**
   - Crear un documento PDF que incluya:
     - Título del informe.
     - Resumen en formato de tabla.
     - Visualizaciones gráficas, como gráficos circulares o de barras.
   - Usar la librería `ReportLab` para personalizar el diseño del informe.

3. **Envío del informe por correo electrónico:**
   - Conectar con un servidor SMTP para el envío de correos.
   - Adjuntar el PDF generado al mensaje.
   - Enviar el informe automáticamente a los destinatarios.

## Tecnologías utilizadas

- **Python:** Lenguaje principal para el desarrollo del proyecto.
- **Librerías utilizadas:**
  - `requests`: Para obtener datos del servicio web.
  - `reportlab`: Para la creación del informe en PDF.
  - `smtplib` y `email`: Para el envío de correos electrónicos con archivos adjuntos.