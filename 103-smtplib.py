import smtplib, ssl

# El puerto indica dónde está escuchando el servidor de email
port = 587
# Especificamos el servidor de correo electrónico
smtp_server = "smtp.ionos.es"
# Introducimos el correo del remitente
sender_email = "python@jocarsa.com"
# Contraseña de la cuenta de correo
password = "ContrasenaPython2023$"

# El mensaje que voy a enviar
message = "Hola desde Python"

# Creamos un entorno en el cual enviamos el correo 
context = ssl.create_default_context()



#Si la conexión se abre correctamente
with smtplib.SMTP(smtp_server, port) as server:
    # Selecciono un receptor
    receiver_email = "jocarsa2@gmail.com"
    # Arranco una sesión segura
    server.starttls(context=context)
    # Inicio sesión en el servidor de correo electrónico
    server.login(sender_email, password)
    # Envío el mensaje
    server.sendmail(sender_email, receiver_email, message)
