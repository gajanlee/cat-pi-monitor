import sys
sys.path.append("./communicate/")
import monitor_pb2
import monitor_pb2_grpc
import base64
import grpc
import time
from photo_utils import get_image_base64_from_path, get_image_base64_from_bytes
from pi_camera import get_camera_handler

def fetch_server_operation():
    while True:
        yield monitor_pb2.MonitorRequest(operation="fetch")

def image_stream():
    camera_handler = get_camera_handler()
    for i, image_byte in enumerate(camera_handler.get_image_bytes_stream()):
        try:
            print(f"transfering image")

            yield monitor_pb2.MonitorData(
                filename=f"{i}.jpg", 
                data=get_image_base64_from_bytes(image_byte),
            )
            time.sleep(2)
        except Exception as ex:
            print(ex)

def run():
    address = "192.168.8.111"
    port = "9963"

    channel = grpc.insecure_channel(f"{address}:{port}")
    stub = monitor_pb2_grpc.MonitorServiceStub(channel)

    # for response in stub.PutMonitorStream(fetch_server_operation()):
    #     (response.mode, response.interval)
    # for _ in get_camera_handler().get_image_bytes_stream():
    #     pass

    response = stub.PutMonitorStream(image_stream())

if __name__ == '__main__':
    run()