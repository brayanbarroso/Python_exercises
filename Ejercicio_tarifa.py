nombre = input("Ingrese el nombre del empleado: ")
estrato = int(input("ingrese el estrato del empleado: "))

if estrato == 1:
    print("La tarifa del usuario " + str(nombre) + "es $10.000 su estrato es: " +str(estrato))
elif estrato == 2:
    print("La tarifa del usuario " + str(nombre) + "es $15.000 su estrato es: " +str(estrato))
elif estrato == 3:
    print("La tarifa del usuario " + str(nombre) + "es $30.000 su estrato es: " +str(estrato))
elif estrato == 4:
    print("La tarifa del usuario " + str(nombre) + "es $50.000 su estrato es: " +str(estrato))
elif estrato == 5:
    print("La tarifa del usuario " + str(nombre) + "es $65.000 su estrato es: " +str(estrato))
else:
    print("Estrato no valido digite un numero de 1 a 5")
    
