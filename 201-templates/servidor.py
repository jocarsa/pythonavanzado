#importo la librería Flask
from flask import Flask
# importo la librería de templates
from flask import render_template

# Creo una variable llamada app que se convierte en un servidor
app = Flask(__name__)

@app.route("/")
def principal():
    return render_template("base.html")
