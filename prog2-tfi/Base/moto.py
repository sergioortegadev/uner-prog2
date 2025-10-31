import vehiculo


class Moto(vehiculo.Vehiculo):

    def __init__(
        self, numero_id, marca, modelo, anio, sucursal_id, estado_id, cilindrada
    ):
        super().__init__(numero_id, marca, modelo, anio, sucursal_id, estado_id)
        self.__cilindrada = cilindrada

    def establecer_cilindrada(self, cilindrada):
        self.__cilindrada = cilindrada

    def obtener_cilindrada(self):
        return self.__cilindrada
    
       # Ejercicio 5
    def __eq__(self, value):
        return super().__eq__(self, value)
    
    def __str__(self):
        return f'Moto -> numero id: {self._Vehiculo__numero_id} - marca: {self._Vehiculo__marca} - modelo: {self._Vehiculo__modelo} - año: {self._Vehiculo__anio} - sucursal id: {self._Vehiculo__sucursal_id} - estado id: {self._Vehiculo__estado_id} - cilindrada: {self.__cilindrada}\n'
