#importo la librería Flask
from flask import Flask

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
    return cabecera+"Esta es la página del blog"

# arrancar servidor con:
# flask --app servidor.py run
