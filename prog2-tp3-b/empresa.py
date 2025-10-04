from empleado import *

# Ejercicio 4
class Empresa:
  def __init__(self, razon_social):
    # Ejercicio 9
    self.__razon_social = razon_social
    self.__productos = []
    self.__empleados = []

  def establecer_razon_social(self, razon_social):
    self.__razon_social = razon_social

  def agregar_producto(self, producto):
    self.__productos.append(producto)

  def remover_producto(self, producto):
    self.__productos.remove(producto)

  # Ejercicio 5
  def alta_empleado(self, empleado):
    legajo = len(self.__empleados) + 1
    empleado.establecer_numero_legajo(legajo)
    self.__empleados.append(empleado)

  # Ejercicio 6
  def baja_empleado(self, empleado):
    for emple in self.__empleados:
      if empleado.obtener_numero_legajo() == emple.obtener_numero_legajo():
        empleado.establecer_estado(Empleado.ESTADO_BAJA)

  def obtener_razon_social(self):
    return self.__razon_social
  
  def obtener_productos(self):
    return self.__productos
  
  # Ejercicio 7
  def obtener_empleados_de_alta(self):
    empleados_alta = []
    for emple in self.__empleados:
      if emple.obtener_estado() == 1:
        empleados_alta.append(emple)
    return empleados_alta
    # empleados_alta = ''.join(str(emple) for emple in empleados_alta)
    # return f'Empleados Alta:\n{empleados_alta}'

  def obtener_empleados_historico(self):
    return self.__empleados
    # empleados_hist = ''.join(str(emple) for emple in self.__empleados)
    # return f'Empleados Historico:\n{empleados_hist}'

 # Ejercicio 8
  def __str__(self):
    productos = ''.join(str(prod) for prod in self.__productos)
    empleados = ''.join(str(emple) for emple in self.obtener_empleados_de_alta())
    return f' Empresa razón social: {self.__razon_social}\n\n Tiene Con productos: \n{productos}\n Empleados de Alta: \n{empleados}\n '

  def __eq__(self, other):
     if (isinstance(other, Empresa)):
       return other.__razon_social == self.__razon_social
     return NotImplemented

