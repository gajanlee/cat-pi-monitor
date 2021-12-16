import grpc
import monitor_pb2
import monitor_pb2_grpc
import time
import cv2
from image_utils import decode_base64_to_bytes
import numpy as np
from PIL import Image
import io

from flask import Response, Flask, render_template

# import bottle
# from bottle import request, response, static_file
# from bottle import post, get, put, delete
# from utils import load_config_json

address = "0.0.0.0"
port = "50000"

channel = grpc.insecure_channel(f"{address}:{port}")
stub = monitor_pb2_grpc.MonitorServiceStub(channel)

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

def request_generator():
    while True:
        yield monitor_pb2.MonitorRequest(operation="fetch")
        time.sleep(1)

def generate():
	# grab global references to the output frame and lock variables
    for data in stub.GetMonitorStream(request_generator()):
        # ensure the frame was successfully encoded
        image_array = np.fromstring(decode_base64_to_bytes(data.data), np.uint8)
        image_array = image_array.reshape(512, 512, -1)
        print(image_array.shape)
        (flag, encodedImage) = cv2.imencode(".jpg", image_array)
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + 
            bytearray(encodedImage) + b'\r\n')


if __name__ == "__main__":
    # bottle.run(server="gunicorn", host="0.0.0.0", port=8083)
    app.run(host="0.0.0.0", port=9999, debug=True,
		threaded=True, use_reloader=False)
