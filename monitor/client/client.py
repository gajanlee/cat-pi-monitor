import argparse
import grpc
from camera import PiCameraHandler
from monitor import monitor_pb2, monitor_pb2, monitor_pb2_grpc
from monitor.photo_utils import get_image_base64_from_bytes
import time

parser = argparse.ArgumentParser(description='run camera capturer')
parser.add_argument('--ip', required=True, help='the ip address of remote grpc server')
parser.add_argument('--port', required=True, default=55000, help='the port of remote grpc server')

args = parser.parse_args()

camera = PiCameraHandler()

def run(ip, port):
    stub = monitor_pb2_grpc.MonitorStub(grpc.insecure_channel(f"{ip}:{port}"))

    for index, image_byte in enumerate(camera.get_image_bytes_stream()):
        try:
            reply = stub.PutMonitorStream(monitor_pb2.MonitorData(
                timestamp = time.time(),
                data = get_image_base64_from_bytes(image_byte),
            ))
        except Exception as ex:
            print(ex)

if __name__ == "__main__":

    run(args.ip, args.port)