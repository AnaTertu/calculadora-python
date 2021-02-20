from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if  (request.method == "GET"):
        return render_template("index.html")
    else:    
        if(request.form["n1"] != "" and request.form["n2"] != ""):
            n1 = request.form["n1"]
            n2 = request.form["n2"]
            option = request.form["option"]
            resultado = 0
            if ((option) == "soma"):
                resultado = int(n1) + int(n2)
                
            elif ((option) == "subtracao"):
                resultado = int(n1) - int(n2)
            
            elif ((option) == "multiplicacao"):
                resultado = int(n1) * int(n2)
                
            elif ((option) == "divisao"):
                resultado = int(n1) // int(n2)
                
            elif ((option) == "porcentagem"):
                resultado = int(n1) % int(n2)

            return render_template("result.html", resultadoDoCalculo=resultado)
        
        else:
                return "informe um valor válido"

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=3333, debug=True)