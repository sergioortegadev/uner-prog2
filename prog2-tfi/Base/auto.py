import vehiculo


class Auto(vehiculo.Vehiculo):

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
  
  def __eq__(self, value):
    return super().__eq__(self, value)
    
  def __str__(self):
    return f'Auto -> numero id: {self.__numero_id} - marca: {self.__marca} - modelo: {self.__modelo} - año: {self.__anio} - sucursal id: {self.__sucursal_id} - estado id: {self.__estado_id} - airbags: {self.__airbags} - frenos abs: {self.__frenos_abs} - caballos de fuerza: {self.__caballos_fuerza}\n'