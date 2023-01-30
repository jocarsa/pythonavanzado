#importo la librería Flask
from flask import Flask

# Creo una variable llamada app que se convierte en un servidor
app = Flask(__name__)

@app.route("/")
def principal():
    return "Soy la página principal"

# arrancar servidor con:
# flask --app servidor.py run
