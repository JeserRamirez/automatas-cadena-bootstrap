from flask import Flask, render_template, request

app = Flask(__name__)


def procesarCadena(entrada):
    # Implement your logic to process the input string
    # For demonstration purposes, let's assume the processing is converting the string to uppercase
    cadenaProcesada = entrada.upper()
    return cadenaProcesada

def checkSintaxisCorrect(entrada):
    if entrada != "":
        return True
    return "Error de sintaxis"


@app.route("/", methods=["GET", "POST"])
def homepage():
    cadenaProcesada = None

    if request.method == "POST":
        entrada = request.form.get("entrada")
        cadenaProcesada = procesarCadena(entrada)

    return render_template("index.html", title="Lenguajes y Automatas II", cadenaProcesada=cadenaProcesada)

@app.route("/analisis-sintactico.html")
def analisis_sintactico():
    # Lógica para mostrar la página de análisis sintáctico
    return render_template("analisis-sintactico.html")

@app.route("/analisis-lexico.html")
def analisis_lexico():
    # Lógica para mostrar la página de análisis sintáctico
    return render_template("analisis-lexico.html")

if __name__ == "__main__":
    app.run(debug=True)

