#!/usr/bin/env python3

# Importamos las librerías necesarias
import os
import datetime
import reports
import emails

def main():
    # Definimos los datos del reporte
    title = "Processed Update on " + str(datetime.date.today())
    paragraph = """
    name: Apple
    weight: 500 lbs
    name: Avocado
    weight: 200 lbs
    """
    
    # Generamos el archivo PDF
    attachment = "/tmp/processed.pdf"
    reports.generate_report(attachment, title, paragraph)

    # Creamos y enviamos el correo electrónico con el archivo adjunto
    message = emails.generate_email(
        from_addr="automation@example.com",
        to_addr="student@example.com",
        subject="Upload Completed - Online Fruit Store",
        body="All fruits are uploaded to our website successfully. A detailed list is attached to this email.",
        attachment=attachment
    )
    emails.send_email(message)

if __name__ == "__main__":
    main()