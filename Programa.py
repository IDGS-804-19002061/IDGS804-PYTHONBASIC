import os

class Operasbas():
    # Propiedades de clase
    num1=0
    num2=0
    res=0

    # Constructor 
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def suma(self):
        self.res = self.num1 + self.num2
        # print(self.res)

    def restar(self):
        self.res = self.num1 - self.num2
        # print(self.res)

    def multi(self):
        self.res = self.num1 * self.num2
        # print(self.res)

    def division(self):
        self.res = self.num1 / self.num2
        # print(self.res)

def suma():
    print("Ingresa el primer valor")
    num1 = int(input())
    print("Ingresa el segundo valor")
    num2 = int(input())
    obj= Operasbas(num1, num2)
    obj.suma()
    print(f"El resultado es: {obj.res}")

def restar():
    print("Ingresa el primer valor")
    num1 = int(input())
    print("Ingresa el segundo valor")
    num2 = int(input())
    obj= Operasbas(num1, num2)
    obj.restar()
    print(f"El resultado es: {obj.res}")

def multi():
    print("Ingresa el primer valor")
    num1 = int(input())
    print("Ingresa el segundo valor")
    num2 = int(input())
    obj= Operasbas(num1, num2)
    obj.multi()
    
    print(f"El resultado es: {obj.res}")

def division():
    print("Ingresa el primer valor")
    num1 = int(input())
    print("Ingresa el segundo valor")
    num2 = int(input())
    obj= Operasbas(num1, num2)
    obj.division()
    print(f"El resultado es: {obj.res}")

def main():
    os.system('cls')
    while True:
        
        print("Selecciona una opcion \n 1.Suma \n 2.Resta \n 3.Multiplicacion \n 4.Division \n 5.Salir")
        opc = input()
        if opc=='1':
            suma()
        elif opc=='2':
            restar()
        elif opc=='3':
            multi()
        elif opc=='4':
            division()
        elif opc=='5':
            break
            print("Fin de programa")

if __name__ =='__main__':
    main()

main()