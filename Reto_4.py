def calcularCosto(alto, ancho, profundo):
      
    volumen = alto * ancho * profundo
    costo = volumen*5
    if alto > 30:
        costo = costo + 2000
    if costo > 10000:
        iva = costo*0.19 
        costo += iva
    else:
        costo = volumen * 5
    return costo
    
def costoTotal(numeroPaquetes, descuento):
    costoParcial = 0
    for i in range(numeroPaquetes):
       alto = float(input())
       ancho = float(input())
       profundo = float(input())

       calcularCosto(alto, ancho, profundo)
       costoParcial += calcularCosto(alto, ancho, profundo)
    
    descuentoPaquete = (costoParcial * descuento) / 100
    costoTotal = costoParcial - descuentoPaquete
    return costoTotal