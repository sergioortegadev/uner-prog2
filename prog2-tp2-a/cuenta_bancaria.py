# Ejercicio 12
class Cuenta_bancaria:
 def __init__(self, n):
  self.numero = n
  self.saldo = 0

 def establecer_numero(self, n):
  self.numero = n

 def realizar_deposito(self, c):
  self.saldo = self.saldo + c
 
 def realizar_extraccion(self, e):
  # Ejercicio 13
  if self.saldo < e:
   return False
  self.saldo = self.saldo - e
  return True
 
 def obtener_numero(self):
  return self.numero
 
 def obtener_saldo(self):
  return self.saldo
 