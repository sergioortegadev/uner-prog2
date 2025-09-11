# Ejercicio 1

class Cancion:
 def __init__(self, nombre, duracion, genero):
  self.nombre = nombre
  self.duracion = duracion
  self.genero = genero

 def establecer_nombre(self, nombre):
  self.nombre = nombre

 def establecer_duracion(self, duracion):
  self.duracion = duracion

 def establecer_genero(self, genero):
  self.genero = genero

 def obtener_nombre(self):
  return self.nombre
 
 def obtener_duracion(self):
  return self.duracion
 
 def obtener_genero(self):
  return self.genero
 
 