#!/usr/bin/env python3

# Importamos las librerías necesarias de reportlab para generar PDFs.
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import datetime

def generate_report(attachment, title, paragraph):
    """Genera un reporte PDF con los detalles de las frutas procesadas."""
    c = canvas.Canvas(attachment, pagesize=letter)
    c.drawString(100, 750, title)  # Título del reporte
    c.drawString(100, 730, paragraph)  # Detalles de las frutas
    c.save()  # Guardamos el archivo PDF

if __name__ == "__main__":
    # Definimos el título y el contenido del reporte
    title = "Processed Update on " + str(datetime.date.today())
    paragraph = """
    name: Apple
    weight: 500 lbs
    name: Avocado
    weight: 200 lbs
    """
    attachment = "/tmp/processed.pdf"  # Ruta del archivo PDF generado
    generate_report(attachment, title, paragraph)