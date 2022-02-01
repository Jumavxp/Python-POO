import os 
os.system('cls')

class Aritmetica:
    """ clase atirmetica para realizar operaciones matematicas basicas"""
    def __init__(self, operandoA, operandoB):
        self.operandoA = operandoA
        self.operandoB = operandoB
        
    def suma(self):
        return self.operandoA + self.operandoB

    def resta(self):
        return self.operandoA - self.operandoB

    def mult(self):
        return self.operandoA * self.operandoB

    def div(self):
        return self.operandoA / self.operandoB


aritmetica1 = Aritmetica(5,3)
print(aritmetica1.suma())
print(aritmetica1.resta())
print(aritmetica1.mult())
print(round(aritmetica1.div(),2))