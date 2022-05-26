alto = input("Ingrese la altura del paquete \n")
ancho = input("Ingrese el ancho del paquete \n")
profundo = input("Ingrese la profundidad del paquete \n")

alto = float(alto)
ancho = float(ancho)
profundo = float(profundo)

volumen = alto * ancho * profundo
costo = volumen *5

print(volumen)
print(costo)
