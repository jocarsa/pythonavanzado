# pip install mysql-connector-python
# Importo el conector
import mysql.connector

# Me conecto al servidor y guardo la conexión
conexion = mysql.connector.connect(
    host = "localhost",
    user = "curso",
    password = "curso",
    port = 3306,
    database = "curso"
    )
# Creo un cursor para ejecutar peticiones
micursor = conexion.cursor()
# Ejecuto una consulta de inserción
micursor.execute('''
INSERT INTO productos
VALUES (
NULL,
"camisa1",
"esta es una buena camisa",
15.34,
"camisa1.jpg",
5)
''')
# Lanzo la consulta
conexion.commit()

