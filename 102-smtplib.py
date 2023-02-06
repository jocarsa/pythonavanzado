import smtplib, ssl

port = 587
smtp_server = "smtp.ionos.es"
sender_email = "python@jocarsa.com"
receiver_email = "info@josevicentecarratala.com"
password = "ContrasenaPython2023$"

message = "Hola desde Python"

context = ssl.create_default_context()

with smtplib.SMTP(smtp_server, port) as server:
    server.starttls(context=context)
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)
