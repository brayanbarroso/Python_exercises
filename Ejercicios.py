num1 = float(input("Escriba un numero \n"))
num2 = float(input("Escriba un numero \n"))


media = (num1 + num2)/2

print("La media de los numeros", num1, "y", num2, "es", media, "\n")
#-------------------------------------------------------------------

peso = float(input("Ingrese su peso:\n"))
altura = float(input("Ingrese su altura: \n"))

imc = peso/(altura*altura)

print("su masa coparal es", round(imc,1))

#-------------------------------------------------------------------------
pies = float(input("Escriba una cantidad de pies \n"))
pulgadas = float(input("Escriba una cantidad de pulgadas \n"))

convesion_pulgadas = pies*12
suma_pulgadas = convesion_pulgadas + pulgadas

total = suma_pulgadas  * 2.54

print(total)


             
