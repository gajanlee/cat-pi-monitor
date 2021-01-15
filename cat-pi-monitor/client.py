from communicate import monitor_pb2
from communicate import monitor_pb2_grpc
import grpc


def fetch_server_operation():
    while True:
        yield monitor_pb2.MonitorRequest(operation="fetch")

def run():
    address = ""
    port = ""

    channel = grpc.insecure_channel(f"{address}:{port}")
    stub = monitor_pb2_grpc.MonitorServiceStub(channel)

    for response in stub.GetOperationStream(fetch_server_operation()):
        (response.mode, response.interval)

if __name__ == '__main__':
    run()