import json

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
        
def costoTotal(listaPaquetes, descuento):
    costoParcial = 0
    for package in listaPaquetes:
       alto = package["ALTO"]
       ancho = package["ANCHO"]
       profundo = package["PROFUNDO"]

       calcularCosto(alto, ancho, profundo)
       costoParcial += calcularCosto(alto, ancho, profundo)
    
    descuentoPaquete = (costoParcial * descuento) / 100
    costoTotal = costoParcial - descuentoPaquete
    print("El costo total es: " +  str(costoTotal))

def run():
    with open('paquetes.json') as file:
        empresa = json.load(file)
    costoTotal(empresa['PAQUETES'], 10)


if __name__ == '__main__':
    run()