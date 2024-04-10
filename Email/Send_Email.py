from dotenv import load_dotenv
from email.message import EmailMessage
import smtplib
import os

load_dotenv()

remitente = os.getenv('USUARIO_EMAIL')
destinatario = ''
mensaje = 'Hola'

email = EmailMessage()
email['From'] = remitente  # Usar llaves {} en lugar de corchetes [] para asignar valores a los campos del email
email['To'] = destinatario
email['Subject'] = 'Email Test'
email.set_content(mensaje)  # Corregido: Llamar al método set_content correctamente

smtp = smtplib.SMTP_SSL('smtp.gmail.com')
smtp.login(remitente, "Weta#ss")
smtp.sendmail(remitente, destinatario, email.as_string())  # Corregido: Agregar comas entre los argumentos
smtp.quit()
