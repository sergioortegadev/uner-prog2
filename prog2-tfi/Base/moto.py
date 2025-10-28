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
    
    def __eq__(self, value):
        return super().__eq__(self, value)
    
    def __str__(self):
        return f'Moto -> numero id: {self.__numero_id} - marca: {self.__marca} - modelo: {self.__modelo} - año: {self.__anio} - sucursal id: {self.__sucursal_id} - estado id: {self.__estado_id} - cilindrada: {self.__cilindrada}\n'
