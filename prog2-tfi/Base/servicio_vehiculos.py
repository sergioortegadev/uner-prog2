from servicio_concesionarias import ServicioConcesionarias

      # Ejercicio 7

class ServicioVehiculos:

    def obtenerVehiculosPorSucursalYEstado(self, id_concesionaria, id_sucursal=None, id_estado=None):
        servicio = ServicioConcesionarias()
        concesionaria_obj = servicio.obtener_por_id(id_concesionaria)
        if not concesionaria_obj:
            return []

        vehiculos = concesionaria_obj.obtener_vehiculos()
        if id_sucursal is not None:
            vehiculos = [v for v in vehiculos if v.obtener_sucursal_id() == int(id_sucursal)]
        if id_estado is not None:
            vehiculos = [v for v in vehiculos if v.obtener_estado_id() == int(id_estado)]

        return vehiculos