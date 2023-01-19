
print("Sumar dos numeros")
num1=int(input("Dame el primer numero"))
num2=int(input("Dame el segundo numero"))
res=num1+num2

print("La suma de {0} + {1} = {2}" .format(num1, num2, res))

if num1 > num2 : 
    print("{} es mayor que {}" .format(num1, num2))
else :
    print("{} es menor que {}" .format(num1, num2))

print("-----------------Nuevo programa-----------------")

edad=int(input("Ingresa tu edad "))
if edad >= 18 : 
    print("Eres mayor de edad")
elif edad == 18 :
    print("Tienes 18  años!!!")
else :
    print("No eres mayor de edad")

'''
AND
OR 
NOT

>, <, <= >= !
'''

valor1=200
valor2=2
valor3=100

if(valor1>100 and valor2>2) or valor3 <2000:
    print("Resultado")