#importo la librería Flask
from flask import Flask
from flask import request

# Creo una variable llamada app que se convierte en un servidor
app = Flask(__name__)

@app.route("/")
def principal():
    articulo = request.args.get('idarticulo')
    return "Voy a cargar el artículo: "+articulo


# arrancar servidor con:
# flask --app servidor.py run
