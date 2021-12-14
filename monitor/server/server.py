# import sys
Path()
# sys.path.append("./communicate/")

import grpc
import monitor_pb2
import monitor_pb2_grpc

from flask import Response, Flask, render_template

# import bottle
# from bottle import request, response, static_file
# from bottle import post, get, put, delete
# from utils import load_config_json

address = "0.0.0.0"
port = "9963"

channel = grpc.insecure_channel(f"{address}:{port}")
stub = monitor_pb2_grpc.MonitorStub(channel)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/live/video")
def live_video():
    return Response(
        generate(),
        mimetype = "multipart/x-mixed-replace; boundary=frame"
    )

def generate():
    for data in stub.GetMonitorStream(monitor_pb2.MonitorRequest(
        timestamp = time.time()
    )):
        data.timestamp

if __name__ == "__main__":
    bottle.run(server="gunicorn", host="0.0.0.0", port=8083)
