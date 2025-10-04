# Ejercicio 2

class Empleado:
 ESTADO_ALTA = 1
 ESTADO_BAJA = 2

 def __init__(self, nombre, apellido):
  # Ejercicio 9
  self.__numero_legajo = 0
  self.__nombre =  nombre
  self.__apellido = apellido
  # Ejercicio 3
  self.__estado = Empleado.ESTADO_ALTA

 def establecer_numero_legajo(self, numero):
  self.__numero_legajo = numero

 def establecer_nombre(self, nombre):
  self.__nombre = nombre

 def establecer_apellido(self, apellido):
  self.__apellido = apellido

 def establecer_estado(self, estado):
  self.__estado = estado

 def obtener_numero_legajo(self):
  return self.__numero_legajo
 
 def obtener_nombre(self):
  return self.__nombre
 
 def obtener_apellido(self):
  return self.__apellido
 
 def obtener_estado(self):
  return self.__estado
 
 # Ejercicio 8
 def __str__(self):
  return f'| Empleado Legajo nº {self.__numero_legajo} | Nombre completo: {self.__nombre} {self.__apellido} | Estado: {self.__estado} |\n'
 
 def __eq__(self, other):
   if (isinstance(other, Empleado)):
     return other.__numero_legajo == self.__numero_legajo
   return NotImplemented