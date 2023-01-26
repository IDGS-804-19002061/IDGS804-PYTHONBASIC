
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

def main():
    obj=Operasbas(3, 4)
    obj.suma()
    print(f"La suma es: {obj.res}")

if __name__ =='__main__':
    main()

    # Metodos de clase
    

    