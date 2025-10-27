from flask import Flask, request, render_template
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
    titulo = "Mi App de Concesionarias"
    # 1. Calcular el tiempo transcurrido
    tiempo_transcurrido_segundos = time.time() - SERVER_START_TIME
    
    # 2. Formatear el tiempo a Horas, Minutos y Segundos
    # Usamos timedelta para un manejo fácil de la conversión de segundos a H:M:S
    td = datetime.timedelta(seconds=int(tiempo_transcurrido_segundos))
    
    # Formato simple (H:MM:SS)
    # Por ejemplo, '0:05:30' o '1:10:00'
    tiempo_funcionamiento_formato = str(td) 

    # 3. Renderizar la plantilla, pasando la variable
    return render_template(
        'index.html', 
        tiempo_funcionamiento=tiempo_funcionamiento_formato, page_title=titulo, server_status="Funciona!"  # <- Variable que usaremos en el HTML
    )

@app.route("/concesionarias/<concesionaria_id>/", methods=["GET"])
def obtener_concesionaria(concesionaria_id):

    servicio = servicio_concesionarias.ServicioConcesionarias()

    concesiaria_encontrada = servicio.obtener_por_id(concesionaria_id)

    if concesiaria_encontrada is None:
        flask.abort(404)

    return f"<pre>{str(concesiaria_encontrada)}</pre>", 200


@app.route(
    "/concesionarias/<concesionaria_id>/clientes/<id_cliente>/total-ventas/",
    methods=["GET"],
)
def obtener_total_ventas_de_cliente(concesionaria_id, id_cliente):

    servicio = servicio_clientes.ServicioClientes()

    total_ventas = servicio.obtener_total_ventas_por_cliente(
        concesionaria_id, id_cliente
    )

    return str(total_ventas), 200


@app.route(
    "/concesionarias/<concesionaria_id>/sucursales/<sucursal_id>/vehiculos/",
    methods=["GET"],
)
def obtener_vehiculos(concesionaria_id, sucursal_id):

    estado_id = flask.request.args.get("estado_id")

    servicio = servicio_vehiculos.ServicioVehiculos()

    vehiculos = servicio.obtener_vehiculos_por_sucursal_y_estado(
        concesionaria_id, sucursal_id, estado_id
    )

    texto_respuesta = "Vehículos:\n  "

    texto_respuesta = texto_respuesta + "\n  ".join(
        str(vehiculo) for vehiculo in vehiculos
    )

    return f"<pre>{texto_respuesta}</pre>", 200
