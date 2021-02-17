import sys
sys.path.append("./communicate/")
import monitor_pb2
import monitor_pb2_grpc
import base64
import grpc
import time
from photo_utils import get_image_base64_from_path


def fetch_server_operation():
    while True:
        yield monitor_pb2.MonitorRequest(operation="fetch")

def image_stream():
    for i in range(5):
        try:
            print(f"transfering {i}th image")

            yield monitor_pb2.MonitorData(
                filename=f"{i}.jpg", 
                data=get_image_base64_from_path("/home/lee/Desktop/test.jpeg"),
            )
            time.sleep(1)
        except Exception as ex:
            print(ex)

def run():
    address = "127.0.0.1"
    port = "9963"

    channel = grpc.insecure_channel(f"{address}:{port}")
    stub = monitor_pb2_grpc.MonitorServiceStub(channel)

    # for response in stub.PutMonitorStream(fetch_server_operation()):
    #     (response.mode, response.interval)

    response = stub.PutMonitorStream(image_stream())

if __name__ == '__main__':
    run()