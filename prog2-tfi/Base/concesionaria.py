class Concesionaria:

    def __init__(self, numero_id, nombre):
        self.__numero_id = numero_id
        self.__nombre = nombre
        self.__clientes = []
        self.__sucursales = []
        self.__vehiculos = []

    def establecer_numero_id(self, numero_id):
        self.__numero_id = numero_id

    def establecer_nombre(self, nombre):
        self.__nombre = nombre

    def agregar_cliente(self, cliente):
        self.__clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.__clientes.remove(cliente)

    def agregar_sucursal(self, sucursal):
        self.__sucursales.append(sucursal)

    def remover_sucursal(self, sucursal):
        self.__sucursales.remove(sucursal)

    def agregar_vehiculo(self, vehiculo):
        self.__vehiculos.append(vehiculo)

    def remover_vehiculo(self, vehiculo):
        self.__vehiculos.remove(vehiculo)

    def obtener_numero_id(self):
        return self.__numero_id

    def obtener_nombre(self):
        return self.__nombre

    def obtener_clientes(self):
        return self.__clientes

    def obtener_sucursales(self, id_sucursal=None):
        if id_sucursal is None:
            return self.__sucursales
        id_sucursal = int(id_sucursal)
        for sucursal in self.__sucursales:
            if int(sucursal.obtener_numero_id()) == id_sucursal:
                return sucursal
        return None


    def obtener_vehiculos(self, id_vehiculo=None):
        if id_vehiculo is None:
            return self.__vehiculos
        
        id_vehiculo = int(id_vehiculo)
        for vehiculo in self.__vehiculos:
            if int(vehiculo.obtener_numero_id()) == id_vehiculo:
                return vehiculo

        return None

   # Ejercicio 5
    def __eq__(self, value):
        if isinstance(value, Concesionaria):
            return self.__numero_id == value.obtener_numero_id()
        else: NotImplemented

    def __str__(self):
        data_clientes = ''.join(str(el) for el in self.__clientes)
        data_sucursales = ''.join(str(el) for el in self.__sucursales)
        data_vehiculos = ''.join(str(el) for el in self.__vehiculos)
        return f'Concesionaria nº: {self.__numero_id} - Nombre: "{self.__nombre}"\n   Listado de sucursales:\n{data_sucursales}\n   Listado de clientes:\n{data_clientes}\n   Listado de vehículos:\n{data_vehiculos}\n'