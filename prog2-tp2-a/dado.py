import random

# Ejercicio 17

class Dado:
 def __init__(self):
  self.ultimo_valor = random.randint(1,6)

 def tirar(self):
  self.ultimo_valor = random.randint(1,6)

 def obtener_ultimo_valor(self):
  return self.ultimo_valor
