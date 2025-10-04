# Ejercicio 1

class Producto:

 def __init__(self, nombre):
  # Ejercicio 9
  self.__nombre = nombre

 def obtenerNombre(self):
  return self.__nombre
 
 # Ejercicio 8
 def __str__(self):
    return f'| Producto nombre: {self.__nombre} |\n'
 
 def __eq__(self, other):
   if (isinstance(other, Producto)):
     return self.__nombre == other.__nombre
   return NotImplemented
