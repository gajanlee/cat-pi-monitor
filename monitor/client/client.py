import argparse
import grpc
from camera import PiCameraHandler, SimpleCameraHandler

from monitor import monitor_pb2, monitor_pb2, monitor_pb2_grpc
from monitor.image_utils import get_image_base64_from_bytes, image_byte_to_cv2_image, add_timestamp_to_image
import time

parser = argparse.ArgumentParser(description='run camera capturer')
parser.add_argument('--ip', required=True, help='the ip address of remote grpc server')
parser.add_argument('--port', required=False, default=50000, help='the port of remote grpc server')
parser.add_argument('--camera', required=False, default="simple", help='the image source')

args = parser.parse_args()

def monitor_data_generator(camera):
    for index, (width, height, image_byte) in enumerate(camera.get_image_byte_stream()):
        image = image_byte_to_cv2_image(width, height, image_byte)
        data = monitor_pb2.MonitorData(
            timestamp = int(time.time()),
            width = width,
            height = height,
            data = get_image_base64_from_bytes(image.tobytes()),
        )
        yield data

def run(ip, port, camera):
    stub = monitor_pb2_grpc.MonitorServiceStub(grpc.insecure_channel(f"{ip}:{port}"))
    for reply in stub.PutMonitorStream(monitor_data_generator(camera)):
        print(reply)

if __name__ == "__main__":
    if args.camera == "simple":
        camera = SimpleCameraHandler()
    elif args.camera == "pi":
        camera = PiCameraHandler()
    else:
        raise Exception(f"unknown camera: {args.camera}")

    run(args.ip, args.port, camera)