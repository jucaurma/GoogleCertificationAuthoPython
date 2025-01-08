#!/usr/bin/env python3

# Importamos las librerías necesarias
import shutil
import psutil
import socket
import emails

def check_cpu_usage():
    """Verifica si el uso de la CPU es mayor al 80%."""
    return psutil.cpu_percent(interval=1) > 80

def check_disk_space():
    """Verifica si el espacio disponible en disco es menor al 20%."""
    total, used, free = shutil.disk_usage("/")
    return (free / total) * 100 < 20

def check_memory():
    """Verifica si la memoria disponible es menor a 100MB."""
    memory = psutil.virtual_memory()
    return memory.available < 100 * 1024 * 1024

def check_localhost_resolution():
    """Verifica si el hostname 'localhost' se resuelve a '127.0.0.1'."""
    return socket.gethostbyname("localhost") != "127.0.0.1"

def generate_error_report(subject, body):
    """Genera un reporte de error por correo electrónico sin adjuntos."""
    message = emails.generate_email(
        from_addr="automation@example.com",
        to_addr="student@example.com",
        subject=subject,
        body=body
    )
    emails.send_email(message)

if __name__ == "__main__":
    # Verificamos cada una de las condiciones
    if check_cpu_usage():
        generate_error_report("Error - CPU usage is over 80%", "Please check your system and resolve the issue as soon as possible.")
    if check_disk_space():
        generate_error_report("Error - Available disk space is less than 20%", "Please check your system and resolve the issue as soon as possible.")
    if check_memory():
        generate_error_report("Error - Available memory is less than 100MB", "Please check your system and resolve the issue as soon as possible.")
    if check_localhost_resolution():
        generate_error_report("Error - localhost cannot be resolved to 127.0.0.1", "Please check your system and resolve the issue as soon as possible.")