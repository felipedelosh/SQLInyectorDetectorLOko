"""
Implementar un módulo que permita filtrar intentos de ataques de SQL Injection
evitando consultas vulnerables y que incorpore funciones para escapar caracteres
anómalos en las cadenas SQL, debe evidenciar la vulnerabilidad de inyección y la
contramedida.

print(a.loginUser("\' or \'1'=\'1", "\' or \'1'=\'1"))
"""

# To create a server service in port 8888
from flask import *
# Import my DATABASE
from DATABASE import *


#Def to app
app = Flask(__name__)

dataBase = DataBase()
# Create a users
dataBase.createUser("loco@loco.loco", "123")
dataBase.createUser("usuario@correo.com", "123")

#First route to probe all, this is GET
@app.route('/login')
def theTest():
    return render_template("index.html")

@app.route('/login/<string:strusername>/<string:strpassword>')
#Example http://localhost:puerto/login/loco/passwrod
#retrun a token if all rigth
def login(strusername, strpassword):
    if dataBase.loginUser(strusername, strpassword):
        templateData = {
           'usuario' : strusername,
           'mensaje' : "Bienvenido a tu banco TEQUEBRAMOS:"
        }
        return render_template("loginExitoso.html", **templateData)
    else:
        templateData = {
           'mensaje' : "Error con tus credenciales"
        }
        return render_template("loginNoExitoso.html", **templateData)



#Start
if __name__ == '__main__':
    app.run(host='0.0.0.0' ,debug=True, port=8888)