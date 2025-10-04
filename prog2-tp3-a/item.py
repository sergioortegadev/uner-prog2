class Item:
  numero_siguiente = 1

  def __init__(self, d):
    self.__descripcion = d
    self.__numero = Item.numero_siguiente
    Item.numero_siguiente = Item.numero_siguiente + 1

  def obtenerNumero(self):
    return self.__numero
  
  def obtenerDescripcion(self):
    return self.__descripcion
  
  def __str__(self):
   return f' Item Nº: {self.__numero} - Desc:{self.__descripcion} |'

  def __eq__(self, other):
   if (isinstance(other, Item)):
     return other.__numero == self.__numero
   return NotImplemented
  