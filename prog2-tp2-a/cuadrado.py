# Ejercicio 5
class Cuadrado:
 instancias_creadas = 0

 def __init__(self, l):
  self.lado = l
  # Ejercicio 6
  Cuadrado.instancias_creadas = Cuadrado.instancias_creadas + 1

 def establecer_lado(self, l):
  self.lado = l
 
 def obtener_lado(self):
  return self.lado
 
 def obtener_area(self):
  return self.lado * self.lado
 
 def obtener_perimetro(self):
  return self.lado * 4
 
