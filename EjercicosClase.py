"""
num1 = int(input("Escriba un número entero: "))
num2 = int(input(f"Escriba un número entero mayor o igual que {num1}: "))

if num1 <= num2:
    for i in range(num1, num2+1):
        if i % 2 == 0:
            print("El numero " + str(i) + " es par")
        else:
            print("El numero " + str(i) + " es impar")
else:
    print(f"Le he pedido un numero mayor que {num1}")
"""
#Contador de numeros negativos
num1 = int(input("Cuantos Valores va Introducir: "))
cont = 0
negativo = 0
positivo = 0
if num1 >= 0:
    while num1 > cont:
        num = int(input("Escibe el numero " +str(cont+1)+":"))
        if num >= 0:
            positivo+=1
        else:
            negativo+=1
        cont+=1
    print("Ha escrito "+ str(negativo) + " numeros negativos")
else:
    print("¡Imposible!")
        
        
    



