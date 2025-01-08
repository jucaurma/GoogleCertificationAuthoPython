#!/usr/bin/env python3

# Importamos las librerías necesarias
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

def generate_email(from_addr, to_addr, subject, body, attachment=None):
    """Genera el correo electrónico y lo prepara para su envío."""
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = to_addr
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))  # Añadimos el cuerpo del mensaje

    # Si hay un archivo adjunto, lo añadimos
    if attachment:
        with open(attachment, 'rb') as att:
            part = MIMEApplication(att.read(), Name="processed.pdf")
            part['Content-Disposition'] = f'attachment; filename="processed.pdf"'
            msg.attach(part)

    return msg

def send_email(message):
    """Envía el correo electrónico a través del servidor SMTP."""
    try:
        with smtplib.SMTP('localhost') as server:
            server.sendmail(message['From'], message['To'], message.as_string())
            print(f"Email sent to {message['To']}")
    except Exception as e:
        print(f"Error sending email: {e}")