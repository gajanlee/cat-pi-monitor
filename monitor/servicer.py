import grpc
from monitor import monitor_pb2, monitor_pb2_grpc
from queue import Queue
from concurrent import futures
from monitor.image_utils import write_base64_to_path


class MonitorServicer(monitor_pb2_grpc.MonitorService):

    def __init__(self):
        self.image_queue = Queue(5)

    def PutMonitorStream(self, request_iterator, context):
        for request in request_iterator:
            # Keep the queue is the newest image
            if self.image_queue.qsize() == 2:
                self.image_queue.get()

            self.image_queue.put(monitor_pb2.MonitorData(
                timestamp = request.timestamp,
                width = request.width,
                height = request.height,
                data = request.data,
            ))

            print(self.image_queue.qsize(), request.timestamp)

            yield monitor_pb2.MonitorReply(
                reply = self.image_queue.qsize(),
            )
    
    def GetMonitorStream(self, request_iterator, context):
        for request in request_iterator:
            if request.operation == "fetch":
                yield self.image_queue.get()


def serve(port):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    monitor_pb2_grpc.add_MonitorServiceServicer_to_server(
        MonitorServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    print("server is running...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve(50000)
