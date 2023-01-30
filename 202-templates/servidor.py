#importo la librería Flask
from flask import Flask
# importo la librería de templates
from flask import render_template
# importo la librería de peticiones
from flask import request

# Creo una variable llamada app que se convierte en un servidor
app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("contacto.html")

@app.route("/procesacontacto/",methods=['POST'])
def procesa():
    nombre = request.form['nombre']
    correo = request.form['email']
    mensaje = request.form['mensaje']
    return nombre+" "+correo+" "+mensaje
