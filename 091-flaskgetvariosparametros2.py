#importo la librería Flask
from flask import Flask
from flask import request

# Creo una variable llamada app que se convierte en un servidor
app = Flask(__name__)

@app.route("/")
def principal():
    articulo = " "
    nombre = " "
    apellido = " "
    try:
        articulo = request.args.get('idarticulo')+" "
    except:
        pass

    try:
        nombre = request.args.get('nombre')+" "
    except:
        pass

    try:
        apellido = request.args.get('apellido')+" "
    except:
        pass
        
    nombre = request.args.get('nombre')
    apellido = request.args.get('apellido')
    return "Hola, "+nombre+" "+apellido+", Voy a cargar el artículo: "+articulo


# arrancar servidor con:
# flask --app servidor.py run
