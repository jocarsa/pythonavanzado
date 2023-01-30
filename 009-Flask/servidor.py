#importo la librería Flask
from flask import Flask
# importo la librería que me permite recuperar parámetros de la url
from flask import request
# Importo el conector
import mysql.connector

conexion = mysql.connector.connect(
    host = "localhost",
    user = "blogpython",
    password = "blogpython",
    port = 3306,
    database = "blogpython"
    )

# Creo una variable llamada app que se convierte en un servidor
app = Flask(__name__)

cabecera= '''
    <html>
        <head>
        </head>
        <body>
        <nav>
            <ul>
                <li><a href="/">Inicio</a></li>
                <li><a href="/sobremi/">Sobre mi</a></li>
                <li><a href="/blog/">Blog</a></li>
                <li><a href="/contacto/">Contacto</a></li>
            </ul>
        </nav>
'''

@app.route("/")
def principal():
    return cabecera+"Soy la página principal"

@app.route("/sobremi/")
def sobremi():
    return cabecera+"Aquí voy a poner la página sobre mi"

@app.route("/contacto/")
def contacto():
    return cabecera+"Esta es la página de contacto"

@app.route("/blog/")
def blog():
    # creo un cursor en la conexión con la base de datos
    micursor = conexion.cursor()
    # ejecuto un comando SQL
    micursor.execute("SELECT * FROM articulos")
    # Meto el resultado en una lista
    miresultado = micursor.fetchall()
    # creo una cadena vacía
    cadena = ""
    # Para cada elemento de la lista
    for resultado in miresultado:
        # Imprimo el resultado en la consola
        cadena = cadena + "<a href='/blog/articulo/?id="+str(resultado[0])+"'>"+resultado[1]+"</a><br>"

    return cabecera+"Esta es la página del blog <br>"+cadena

@app.route("/blog/articulo/")
def articulo():
    # cojo un parametro de la url y lo pongo en una variable
    articulo = request.args.get('id')+" "
    # utilizo esa variable para sacarla por pantalla
    return cabecera+"Esta es el articulo "+articulo

# arrancar servidor con:
# flask --app servidor.py run
