#importo la librería Flask
from flask import Flask
# importo la librería que me permite recuperar parámetros de la url
from flask import request
# Importo el conector
import mysql.connector
# importo la librería de templates
from flask import render_template

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
    
'''

@app.route("/")
def principal():
    return render_template("principal.html")

@app.route("/sobremi/")
def sobremi():
    return render_template("base.html")

@app.route("/contacto/")
def contacto():
    return render_template("contacto.html")

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
    articulo = request.args.get('id')
    # creo un cursor en la conexión con la base de datos
    micursor = conexion.cursor()
    # ejecuto un comando SQL
    micursor.execute("SELECT * FROM articulos WHERE Identificador = "+str(articulo))
    # Meto el resultado en una lista
    miresultado = micursor.fetchall()
    # Para cada elemento de la lista
    for resultado in miresultado:
        # Imprimo el resultado en la consola
        cadena = "<h3>"+resultado[1]+"</h3><time>"+resultado[4]+"</time><p>"+resultado[2]+"</p><img src='"+resultado[3]+"'>"
    # utilizo esa variable para sacarla por pantalla
    return cabecera+cadena

# arrancar servidor con:
# flask --app servidor.py run
