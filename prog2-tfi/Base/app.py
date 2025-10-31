from flask import Flask, request, render_template, abort
import servicio_concesionarias
import servicio_clientes
import servicio_vehiculos
import time
import datetime

app = Flask(__name__)
SERVER_START_TIME = time.time() # tiempo inicio server

@app.route("/", methods=["GET"])
def index():
    print(f' -> Indicador de tráfico. Time: {time.time()} | Tráfico entrante desde la IP: {request.remote_addr}')
    titulo = "App Concesionarias - Prog2 TFI - UNER"
    tiempo_transcurrido_segundos = time.time() - SERVER_START_TIME
    
    td = datetime.timedelta(seconds=int(tiempo_transcurrido_segundos))
    
    tiempo_funcionamiento_formato = str(td) 

    return render_template(
        'index.html', 
        tiempo_funcionamiento=tiempo_funcionamiento_formato, page_title=titulo, server_status="Funciona!" 
    )

@app.route("/concesionarias/<concesionaria_id>/", methods=["GET"])
def obtener_concesionaria(concesionaria_id):

    servicio = servicio_concesionarias.ServicioConcesionarias()

    concesiaria_encontrada = servicio.obtener_por_id(concesionaria_id)

    if concesiaria_encontrada is None:
        abort(404)

    return render_template(
    "datos.html",
    page_title="Concesionaria",
    titulo_datos=f"Concesionaria con ID {concesionaria_id}",
    contenido=str(concesiaria_encontrada),
    ), 200



@app.route(
    "/concesionarias/<concesionaria_id>/clientes/<id_cliente>/total-ventas/",
    methods=["GET"],
)
def obtener_total_ventas_de_cliente(concesionaria_id, id_cliente):

    servicio = servicio_clientes.ServicioClientes()

    total_ventas = servicio.obtenerTotalVentasPorCliente(
        concesionaria_id, id_cliente
    )

    return render_template(
    "datos.html",
    page_title="Total Ventas",
    titulo_datos=f"Total de ventas del cliente con ID {id_cliente}",
    contenido=f"${total_ventas}",
    ), 200


@app.route(
    "/concesionarias/<concesionaria_id>/sucursales/<sucursal_id>/vehiculos/",
    methods=["GET"],
)
def obtener_vehiculos(concesionaria_id, sucursal_id):

    estado_id = int(request.args.get("estado_id"))

    servicio = servicio_vehiculos.ServicioVehiculos()

    vehiculos = servicio.obtenerVehiculosPorSucursalYEstado(
        concesionaria_id, sucursal_id, estado_id
    )

    texto_respuesta = "Vehículos:\n  "

    texto_respuesta = texto_respuesta + "\n  ".join(
        str(vehiculo) for vehiculo in vehiculos
    )

    texto_respuesta = "\n".join(str(v) for v in vehiculos)

    return render_template(
        "datos.html",
        page_title="Vehículos",
        titulo_datos=f"Vehículos en estado ID {estado_id} – Sucursal {sucursal_id}",
        contenido=texto_respuesta,
    ), 200

