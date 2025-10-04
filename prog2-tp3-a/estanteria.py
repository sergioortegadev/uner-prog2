class Estanteria:
 numero_siguiente = 1

 def __init__(self):
  self.__cajas = []
  self.__numero = Estanteria.numero_siguiente
  Estanteria.numero_siguiente = Estanteria.numero_siguiente + 1

 def agregarCaja(self, caja):
  self.__cajas.append(caja)

 def removerCaja(self, caja):
  self.__cajas.remove(caja)

 def obtenerNumero(self):
  return self.__numero 
 
 def obtenerCajas(self):
  return self.__cajas
 
 def __str__(self):
  cajas = ' '.join(str(caja) for caja in self.__cajas)
  return f' Estanteria Nº:{self.__numero}\nCajas: {cajas}\n'
 
def __eq__(self, other):
   if (isinstance(other, Estanteria)):
     return other.__numero == self.__numero
   return NotImplemented