def peso_a_euro(valor):
    euros = valor / 4500
    return euros

print (peso_a_euro(50000))


def procesar_dato(peso, volumen):
    if (peso < 2) and (volumen < 0.027):
        return True 
    else:
        return False
    
print (procesar_dato(5, 3))


def par_impar(valor):
    if valor % 2 == 0:
        return True
    else:
        return False

print (par_impar(24))


