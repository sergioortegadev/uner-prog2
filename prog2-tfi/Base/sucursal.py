class Sucursal:

  def __init__(self, numero_id, direccion):
    self.__numero_id = numero_id
    self.__direccion = direccion
    self.__ventas = []

  def establecerNumeroId(self, numero_id):
    self.__numero_id = numero_id
  
  def establecerDireccion(self, direccion):
    self.__direccion = direccion

  def agregarVenta(self, venta):
    pass
  
  def removerVenta(self, venta):
    pass
  
  def obtenerNumeroId(self):
    return self.__numero_id
  
  def obtenerDireccion(self):
    return self.__direccion
  
  def obtenerVentas(self):
    return self.__ventas
  
  def __eq__(self, value):
    if isinstance(value, Sucursal):
      return self.__numero_id == value.obtenerNumeroId()
    else: NotImplemented
  
  def __str__(self):
    data_ventas = ''.join(str(el) for el in self.__ventas)
    return f'Sucursal nº: {self.__numero_id} - dirección: {self.__direccion}\n   Tiene estas ventas:\n{data_ventas}\n'