from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    if(request.method == "GET"):
        return render_template("index.html")
    else:
        if(request.form["n1"] != "" and request.form["n2"] != ""):
            n1 = request.form["n1"]
            n2 = request.form["n2"]

            if (request.form["option"] == "soma"):
                soma = int(n1) + int(n2)
                return str(soma)
            elif (request.form["option"] == "subtracao"):
                subtracao = int(n1) - int(n2)
                return str(subtracao)
            elif (request.form["option"] == "multiplicacao"):
                multipicacao = int(n1) * int(n2)
                return str(multipicacao)
            elif (request.form["option"] == "divisao"):
                divisao = int(n1) / int(n2)
                return str(divisao)
        else:
            return render_template("error.html")

@app.errorhandler(404)
def not_found(error):
    return render_template("error.html")

app.run(port=9000, debug=True)

# class App():
#     def _init_(self):
#         self.window = sg.Window('PyCalculator', layout=layout, margin=(0, 0))
#         self.result = 0
#         self.oper = ''
#         self.window.read(timeout=1)
#     for i in range(1, 5):
#         for button in layout[i]:
#             button.expand(expand_x=True, expand y=True)

#     def about(self):
#         sg.popup('About', 'just an example', 'contact me')

#     def reulter(self):
#         if self.oper = '+':
#             return float(self.result) + float(self.values['_BOX_'])
#         if self.oper = '-':
#             return float(self.result) -float(self.values['_BOX_'])
#         if self.oper = '*':
#             return float(self.result) * float(self.values['_BOX_'])
#         if self.oper = '/':
#             return float(self.result) / float(self.values['_BOX_'])