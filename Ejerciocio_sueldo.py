nombre = input("Ingrese el nombre del empleado: ")
salario = float(input("ingrese el salario del empleado: "))

sub_trans = 100000

if salario <= 900000:
    print("el emplado tiene derecho a subsidio de transporte")
    print ("sueldo total $",salario + sub_trans)
else:
    print("el emplado no tiene derecho a subsidio de transporte")
    print ("sueldo total $",salario)
