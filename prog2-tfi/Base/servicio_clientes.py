from servicio_concesionarias import ServicioConcesionarias

   # Ejercicio 6
class ServicioClientes:
    def obtenerTotalVentasPorCliente(self, id_concesionaria, id_cliente):
        servicio = ServicioConcesionarias()
        concesionaria = servicio.obtener_por_id(id_concesionaria)

       
        if concesionaria is None:
            return 0
        
        
        clientes = concesionaria.obtener_clientes()

       
        cliente_encontrado = any(
            cliente.obtenerNumeroId() == id_cliente
            for cliente in clientes
        )
        if not cliente_encontrado:
            return 0
        
        total = 0

        
        for sucursal in concesionaria.obtener_sucursales():
            ventas = sucursal.obtenerVentas()  
            for venta in ventas:
                if venta.obtenerClienteId() == id_cliente:
                    total += int(venta.obtenerMonto())

        return total