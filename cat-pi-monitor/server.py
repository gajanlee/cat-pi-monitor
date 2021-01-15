import grpc
import sys
from communicate import monitor_pb2
from communicate import monitor_pb2_grpc
from concurrent import futures
from utils import load_config_json

class Monitor(monitor_pb2_grpc.MonitorService):

    def __init__(self):
        pass

    def PutMonitorStream(self, request, context):
        pass

    def PutMonitorSummary(self, requeset, context):
        pass

def serve():
    config = load_config_json(sys.argv[1])
    port = config.service.port

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    monitor_pb2_grpc.add_MonitorServiceServicer_to_server(
        Monitor(), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
