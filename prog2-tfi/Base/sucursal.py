class Sucursal:
     # Ejercicio 1

  def __init__(self, numero_id, direccion):
    self.__numero_id = numero_id
    self.__direccion = direccion
    self.__ventas = []

  def establecer_numero_id(self, numero_id):
    self.__numero_id = numero_id

  def establecer_direccion(self, direccion):
    self.__direccion = direccion

  def agregar_venta(self, venta):
    self.__ventas.append(venta)
  
  def remover_venta(self, venta):
    if venta in self.__ventas:
      self.__ventas.remove(venta)

  def obtener_numero_id(self):
    return self.__numero_id

  def obtener_direccion(self):
    return self.__direccion

  def obtener_ventas(self):
    return self.__ventas
  
     # Ejercicio 5
  def __eq__(self, value):
    if isinstance(value, Sucursal):
      return self.__numero_id == value.obtener_numero_id()
    else: NotImplemented
  
  def __str__(self):
    data_ventas = ''.join(str(el) for el in self.__ventas)
    return f'Sucursal nº: {self.__numero_id} - dirección: {self.__direccion}\n   Tiene estas ventas:\n{data_ventas}\n'