#importo la librería Flask
from flask import Flask

# Creo una variable llamada app que se convierte en un servidor
app = Flask(__name__)

@app.route("/")
def principal():
    return "Soy la página principal"

@app.route("/sobremi/")
def sobremi():
    return "Aquí voy a poner la página sobre mi"

# arrancar servidor con:
# flask --app servidor.py run
