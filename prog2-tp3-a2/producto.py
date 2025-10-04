class Producto:
 ESTADO_ALTA = 1
 ESTADO_BAJA = 2

 def __init__(self, nombre):
  self.codigo = 1
  self.nombre = nombre
  self.estado = Producto.ESTADO_ALTA

 def establecer_nombre(self, nombre):
  self.nombre = nombre

 def establecer_codigo(self, codigo):
  self.codigo = codigo

 def establecer_estado(self, estado):
  self.estado = estado
  
 def obtener_nombre(self):
  return self.nombre
 
 def obtener_codigo(self):
  return self.codigo
 
 def obtener_estado(self):
  return self.estado
 
 def __str__(self):
  return f'| Codigo: {self.codigo} | Nombre: {self.nombre} | Estado: {self.estado} |\n'
 
 def __eq__(self, other):
  if(isinstance(other, Producto)):
   return other.obtener_codigo() == self.obtener_codigo()
  return NotImplemented
