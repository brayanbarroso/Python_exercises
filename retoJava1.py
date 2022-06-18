def calcularCostoAlmacenamiento(refigerado, valorBase):
  valorTotal = 1
  if (refigerado == True):
    valorTotal = valorBase * 1.30
  else:
    valorTotal = valorBase * 1.15
  
  return valorTotal

def run():
  rg = bool(input("Esta Refigerado el medicamento: \n True = si \n False = no \n"))
 
  vb = float(input("Ingrese el valor base del medicamento \n "))
  print(calcularCostoAlmacenamiento(rg,vb ))


if __name__ == '__main__':
  run()