# Importo las librerías
import sys
import os
import re
from smtplib import SMTP_SSL as SMTP 
from email.mime.text import MIMEText

# Declaro variables de conexión
servidor = 'smtp.ionos.es'
remitente =     'python@jocarsa.com'
detinatario = ['info@josevicentecarratala.com']
usuario = "python@jocarsa.com"
contrasena = "ContrasenaPython2023$"
tipocorreo = 'plain'

contenido="""\
Si estas viendo esto es que te he enviado un correo desde Python
"""

asunto="Enviado desde Python"


try:
    mensaje = MIMEText(contenido, tipocorreo)
    mensaje['Subject']= asunto
    mensaje['From'] = remitente 

    conexion = SMTP(servidor)
    conexion.set_debuglevel(False)
    conexion.login(usuario, contrasena)
    try:
        conexion.sendmail(remitente, detinatario, mensaje.as_string())
    finally:
        conexion.quit()

except:
    sys.exit( "error de envío; %s" % "CUSTOM_ERROR" ) 
