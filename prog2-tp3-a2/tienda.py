import producto

class Tienda:
 def __init__(self):
  self.productos = []

 def agregar_productos(self, producto_param):
  codigo = 1
 
  for prod in self.productos:
   if (prod.obtener_codigo() >= codigo):
    codigo = prod.obtener_codigo() + 1

  producto_param.establecer_codigo(codigo)
  self.productos.append(producto_param)

 def remover_productos(self, producto_param):
  for prod in self.productos:
   if producto_param == prod:
    prod.establecer_estado(producto.Producto.ESTADO_BAJA)

 def __str__(self):
  productos = ''.join(str(prod) for prod in self.productos )
  return f'Productos de la tienda:\n{productos}'
