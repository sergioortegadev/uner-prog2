import servicio_concesionarias


class ServicioClientes:

  def obtenerTotalVentasPorCliente(concesionaria_id, cliente_id):
    if (servicio_concesionarias.ServicioConcesionarias.obtener_por_id(concesionaria_id)):
      pass
    return 0
