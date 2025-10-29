import vehiculo


class Auto(vehiculo.Vehiculo):
  
  # Ejericio 3

  def __init__(self, numero_id, marca, modelo, anio, sucursal_id, estado_id, airbags, frenos_abs, caballos_fuerza):
    super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
    self.__airbags = airbags
    self.__frenos_abs = frenos_abs
    self.__caballos_fuerza = caballos_fuerza


  def establecerAirbags(self, airbags):
    self.__airbags = airbags

  def establecerFrenosAbs(self, frenos_abs):
    self.__frenos_abs = frenos_abs

  def establecerCaballosFuerza(self, caballos_fuerza):
    self.__caballos_fuerza = caballos_fuerza

  def obtenerAirbags(self):
    return self.__airbags
  
  def obtenerFrenosAbs(self):
    return self.__frenos_abs
  
  def obtenerCaballosFuerza(self):
    return self.__caballos_fuerza
  
     # Ejercicio 5
  def __eq__(self, value):
    return super().__eq__(self, value)
    
  def __str__(self):
    return f'Auto -> numero id: {self._Vehiculo__numero_id} - marca: {self._Vehiculo__marca} - modelo: {self._Vehiculo__modelo} - año: {self._Vehiculo__anio} - sucursal id: {self._Vehiculo__sucursal_id} - estado id: {self._Vehiculo__estado_id} - airbags: {self.__airbags} - frenos abs: {self.__frenos_abs} - caballos de fuerza: {self.__caballos_fuerza}\n'