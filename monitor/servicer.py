import grpc
from monitor import monitor_pb2, monitor_pb2_grpc
import time
from concurrent import futures
from monitor.image_utils import write_base64_to_path


class MonitorServicer(monitor_pb2_grpc.MonitorService):

    def __init__(self):
        image_queue = Queue()

    def PutMonitorStream(self, request_iterator, context):
        for request in request_iterator:
            timestamp = request.timestamp
            base64_image = request.data

            image_queue.push_image(timestamp, base64_image)

            yield monitor_pb2.MonitorReply(
                reply = queue.count,
            )
    
    def GetMonitorStream(self, request_iterator, context):
        for request in request_iterator:
            request.timestamp
            if request.operation == "fetch":
                image = image_queue.pop()
                yield monitor_pb2.MonitorData(
                    image.timestamp,
                    image.base64,
                )


def serve(port):
    port = 50000
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    monitor_pb2_grpc.add_MonitorServiceServicer_to_server(
        MonitorServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    print("server is running...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
