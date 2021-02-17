import sys
sys.path.append("./communicate/")

import grpc
import monitor_pb2
import monitor_pb2_grpc

import bottle
from bottle import request, response, static_file
from bottle import post, get, put, delete
from utils import load_config_json

address = "192.168.8.111"
port = "9963"

channel = grpc.insecure_channel(f"{address}:{port}")
stub = monitor_pb2_grpc.MonitorServiceStub(channel)

# for response in stub.PutMonitorStream(fetch_server_operation()):
#     (response.mode, response.interval)
# for _ in get_camera_handler().get_image_bytes_stream():
#     pass


app = application = bottle.default_app()

_names = set()                    # the set of names

@get('/index')
def index_page():
    return static_file("index.html", root="./pages/")

@get('/api/realtime/image')
def realtime_image():
    response = stub.GetRealtimeImage(monitor_pb2.MonitorRequest(operation=1))
    print(response.data)

    return {
        "data": "very good"
    }

if __name__ == "__main__":
    bottle.run(server="gunicorn", host="0.0.0.0", port=8083)
