# Ejercicio 5

class Circulo:
 pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

 def __init__(self, radio):
  self.radio = radio

 def establecer_radio(self, radio):
  self.radio = radio

 def obtener_radio(self):
  return self.radio
 
 def obtener_diametro(self):
  return self.radio * 2
 
 def obtener_area(self):
  return Circulo.pi * self.radio ** 2
 
 def obtener_perimetro(self):
  return Circulo.pi * self.radio * 2
 
 