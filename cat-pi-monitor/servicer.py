import sys
sys.path.append("./communicate/")
import grpc
import monitor_pb2
import monitor_pb2_grpc
from concurrent import futures
from utils import load_config_json
from photo_utils import write_base64_to_path

class MonitorServicer(monitor_pb2_grpc.MonitorService):

    def __init__(self):
        pass

    def PutMonitorStream(self, request_iterator, context):
        for request in request_iterator:
            filename = request.filename
            binary_pic = request.data
            print(filename)
            
            # image = np.fromstring(filename, np.uint8).reshape(480, 640, 3)
            # image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            # cv2.imwrite(filename, image)

            # write_base64_to_path(request.data, "/home/lee/Desktop/1.jpg")
        
        
        return monitor_pb2.MonitorSummary(
            start_time="1000",
            end_time="20000",
            data="3",
        )

    def PutMonitorSummary(self, request, context):
        pass

    def GetOperationStream(self, request, context):
        pass

def serve():
    config = load_config_json(sys.argv[1])
    port = config.service.port

    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    monitor_pb2_grpc.add_MonitorServiceServicer_to_server(
        MonitorServicer(), server)
    server.add_insecure_port(f"[::]:{port}")
    print("server is running...")
    server.start()
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
