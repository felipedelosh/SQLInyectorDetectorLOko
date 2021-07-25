"""
Loko SQLIYECC proyector

Este modulo se encarga de verificar una consulta es segura basada en reglas
rules.txt

1 -> Dado una consulta ejemplo se comprara que no tenga argumentos adiccionales.

Ejemplo:

consulta 1: select * from tabla where id=1  
consulta 2: select * from tabla where id='' or '1' = '1' 

>> 2 no pasa la prueba por que contiene argumentos adicionales (or)

"""

class LOKOSQLPROTECTOR:
    def __init__(self) -> None:
        self.reglas = self.loadRules()


    def getSentencesZero(self):
        return {
            "select" : 0,
            "from": 0,
            "where" : 0,
            "and": 0,
            "or": 0
        }

    def getConditionalsZero(self):
        return {
            "=" : 0,
            "%" : 0,
            ">" : 0,
            "<" : 0,
        }


    def loadRules(self):
        try:
            rules = {}
            key = ""
            value = ""

            f = open('rules.txt', 'r', encoding="UTF-8")

            contador = 0
            for i in f.read().split("\n"):
                if i.strip() != "":
                    if contador%2 == 0:
                        key = i
                        rules[key] = ""
                    else:
                        value = i
                        rules[key] = value

                    contador = contador + 1

            return rules
        except:
            return {}

    def verifySQL(self, type, sql):
        if type == "login":
            return self.verifyLogin(sql)

    def verifyLogin(self, SQL):
        """
        Compare if SQL is like rules.txt (login) 
        
        the SQL is evaluate in 3 test
        1 -> how much words have
        2 -> how many sentesces execute
        3 -> how conditionals have 

        if no have problems return true and continue
        """
        test = 0

        # Se verifica que la consulta tenga la misma cantidad de palabras que la regla
        if len(SQL.split(" ")) != len(self.reglas["login"].split(" ")):
            test = test + 1

        # Se verifica que la consulta tenga la misma cantidad de sentencias
        sqlLogin = self.getSentencesZero()
        for i in self.reglas["login"].split(" "):
            if i in sqlLogin:
                sqlLogin[i] = sqlLogin[i] + 1

        sqlIN = self.getSentencesZero()
        for i in SQL.split(" "):
            if i in sqlIN:
                sqlIN[i] = sqlIN[i] + 1

        if sqlLogin != sqlIN:
            test = test + 1

        #Se verifica que la consulta tenga la misma cantidad de condicionales
        sqlLogin = self.getConditionalsZero()
        for i in self.reglas["login"].split(" "):
            if i in sqlLogin:
                sqlLogin[i] = sqlLogin[i] + 1

        sqlIN = self.getConditionalsZero()
        for i in SQL.split(" "):
            if i in sqlIN:
                sqlIN[i] = sqlIN[i] + 1

        if sqlLogin != sqlIN:
            test = test + 1

        return test == 0


"""
a = LOKOSQLPROTECTOR()

print("Consulta 1")
a.verifySQL("login", "select * from user where username=\'loco\' and password=\'123\'")
print("Consulta 2")
a.verifySQL("login", "select * from user where username=\'\' or '1'='1' and password=\'\' or \'1\'=\'1\';")
"""

