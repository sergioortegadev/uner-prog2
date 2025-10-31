class Venta:
  
  # Ejercicio 4

  def __init__(self, numero_id, fecha, cliente_id, vehiculo_id, monto):
    self.__numero_id = numero_id
    self.__fecha = fecha
    self.__cliente_id = cliente_id
    self.__vehiculo_id = vehiculo_id
    self.__monto = monto

  def establecerNumeroId(self, numero_id):
    self.__numero_id = numero_id
  
  def establecerFecha(self, fecha):
    self.__fecha = fecha

  def establecerClienteId(self, cliente_id):
    self.__cliente_id = cliente_id

  def establecerVehiculoId(self, vehiculo_id):
    self.__vehiculo_id = vehiculo_id

  def establecerMonto(self, monto):
    self.__monto = monto

  def obtenerNumeroId(self):
    return self.__numero_id 
  def obtenerFecha(self):
    return self.__fecha
  def obtenerClienteId(self):
    return self.__cliente_id
  def obtenerVehiculoId(self):
    return self.__vehiculo_id
  def obtenerMonto(self):
    return self.__monto

   # Ejercicio 5
  def __eq__(self, value):
    if isinstance(value, Venta):
      return self.__numero_id == value.obtenerNumeroId()
    else: NotImplemented
  
  def __str__(self):
    return f'Venta -> nº: {self.__numero_id} - fecha: {self.__fecha} - cliente id: {self.__cliente_id} - vehículo id: {self.__vehiculo_id} - monto: {self.__monto}\n'