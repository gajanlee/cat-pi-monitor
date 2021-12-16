import argparse
import grpc
from camera import PiCameraHandler, SimpleCameraHandler

from monitor import monitor_pb2, monitor_pb2, monitor_pb2_grpc
from monitor.image_utils import get_image_base64_from_bytes
import time

parser = argparse.ArgumentParser(description='run camera capturer')
parser.add_argument('--ip', required=True, help='the ip address of remote grpc server')
parser.add_argument('--port', required=False, default=55000, help='the port of remote grpc server')

args = parser.parse_args()

# camera = PiCameraHandler()
camera = SimpleCameraHandler()


def generator():
    for index, (width, height, image_byte) in enumerate(camera.get_image_byte_stream()):
        yield monitor_pb2.MonitorData(
            timestamp = int(time.time()),
            width = width,
            height = height,
            data = get_image_base64_from_bytes(image_byte),
        )

def run(ip, port):
    stub = monitor_pb2_grpc.MonitorServiceStub(grpc.insecure_channel(f"{ip}:{port}"))
    for reply in stub.PutMonitorStream(generator()):
        print(reply)

if __name__ == "__main__":
    run(args.ip, args.port)