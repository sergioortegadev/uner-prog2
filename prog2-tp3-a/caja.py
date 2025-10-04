class Caja:
 numero_siguiente = 1

 def __init__(self, al, an, pr, ma):
  self.__alto = al
  self.__ancho = an
  self.__profundidad = pr
  self.__material = ma
  self.__items = []
  self.__numero = Caja.numero_siguiente
  Caja.numero_siguiente = Caja.numero_siguiente + 1

 def establecerAlto(self, alto):
  self.__alto = alto
 def establecerAncho(self, ancho):
  self.__ancho = ancho
 def establecerProfundidad(self, profundidad):
  self.__profundidad = profundidad
 def establecerMaterial(self, material):
  self.__material = material

 def agregarItem(self, item):
  self.__items.append(item)

 def removerItem(self, item):
  self.__items.remove(item)
 
 def obteneNumero(self):
  return self.__numero
 
 def obtenerDimensiones(self):
  return f'Alto: {self.__alto} - Ancho {self.__ancho} - Profundidad: {self.__profundidad}'
 
 def obtenerItems(self):
  return self.__items
 
 def obtenerMaterial(self):
  return self.__material
 
 def __str__(self):
  items = ','.join(str(item) for item in self.__items)
  return f' Caja Nº: {self.__numero} - Dimensiones: {self.obtenerDimensiones()} - Material: {self.__material}. Items: {items} |'
 
def __eq__(self, other):
   if (isinstance(other, Caja)):
     return other.__numero == self.__numero
   return NotImplemented