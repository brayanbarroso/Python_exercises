alto = float(input("Ingrese la altura del paquete \n"))
ancho = float(input("Ingrese el ancho del paquete \n"))
profundo = float(input("Ingrese la profundidad del paquete \n"))

volumen = alto * ancho * profundo

if alto > 30:
    costo = volumen * 5 + 2000
    if costo > 10000:
        iva = costo * 0.19
        costo = costo + iva
else:
    costo = volumen * 5
    if costo > 10000:
        iva = costo * 0.19
        costo = costo + iva

print(volumen)
print(costo)
        






