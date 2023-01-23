from flask import Flask
app = Flask(__name__)

@app.route("/")

def run():
    cadena = ""
    cadena = cadena + '''
        <style>
            .dia{width:100px;height:100px;border:1px solid black;float:left;}
        </style>
    '''
    for dia in range(0,31):
        cadena = cadena + "<div class='dia'>"+str(dia)+"</div>"
    return cadena
