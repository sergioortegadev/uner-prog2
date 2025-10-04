class Deposito:
 numero_siguiente = 1

 def __init__(self):
  self.__estanterias = []
  self.__numero = Deposito.numero_siguiente
  Deposito.numero_siguiente = Deposito.numero_siguiente + 1

 def agregarEstanteria(self, estanteria):
  self.__estanterias.append(estanteria)

 def removerEstanteria(self, estanteria):
  self.__estanterias.remove(estanteria)

 def obtenerNumero(self):
  return self.__numero
 
 def obtenerEstanterias(self):
  return self.__estanterias
 
 def __str__(self):
  estanteria = ','.join(str(estanteria) for estanteria in self.__estanterias)
  return f' Deposito Nº: {self.__numero}\nEstanterias: {estanteria}'
 
 # def __repr__(self):
 #  return f'Deposito: {self.__numero}'
 
 def __eq__(self, other):
  if (isinstance(other, Deposito)):
   return other.__numero == self.__numero
  return NotImplemented