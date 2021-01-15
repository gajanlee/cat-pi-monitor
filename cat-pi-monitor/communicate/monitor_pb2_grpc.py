# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import monitor_pb2 as monitor__pb2


class MonitorServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.PutMonitorStream = channel.unary_stream(
                '/Monitor.MonitorService/PutMonitorStream',
                request_serializer=monitor__pb2.MonitorRequest.SerializeToString,
                response_deserializer=monitor__pb2.MonitorData.FromString,
                )
        self.PutMonitorSummary = channel.unary_unary(
                '/Monitor.MonitorService/PutMonitorSummary',
                request_serializer=monitor__pb2.MonitorRequest.SerializeToString,
                response_deserializer=monitor__pb2.MonitorSummary.FromString,
                )
        self.GetOperationStream = channel.stream_stream(
                '/Monitor.MonitorService/GetOperationStream',
                request_serializer=monitor__pb2.MonitorRequest.SerializeToString,
                response_deserializer=monitor__pb2.MonitorOperation.FromString,
                )


class MonitorServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def PutMonitorStream(self, request, context):
        """The monitor is in local network, and put the monitor stream to the server
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def PutMonitorSummary(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def GetOperationStream(self, request_iterator, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MonitorServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'PutMonitorStream': grpc.unary_stream_rpc_method_handler(
                    servicer.PutMonitorStream,
                    request_deserializer=monitor__pb2.MonitorRequest.FromString,
                    response_serializer=monitor__pb2.MonitorData.SerializeToString,
            ),
            'PutMonitorSummary': grpc.unary_unary_rpc_method_handler(
                    servicer.PutMonitorSummary,
                    request_deserializer=monitor__pb2.MonitorRequest.FromString,
                    response_serializer=monitor__pb2.MonitorSummary.SerializeToString,
            ),
            'GetOperationStream': grpc.stream_stream_rpc_method_handler(
                    servicer.GetOperationStream,
                    request_deserializer=monitor__pb2.MonitorRequest.FromString,
                    response_serializer=monitor__pb2.MonitorOperation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'Monitor.MonitorService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MonitorService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def PutMonitorStream(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_stream(request, target, '/Monitor.MonitorService/PutMonitorStream',
            monitor__pb2.MonitorRequest.SerializeToString,
            monitor__pb2.MonitorData.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def PutMonitorSummary(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/Monitor.MonitorService/PutMonitorSummary',
            monitor__pb2.MonitorRequest.SerializeToString,
            monitor__pb2.MonitorSummary.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def GetOperationStream(request_iterator,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.stream_stream(request_iterator, target, '/Monitor.MonitorService/GetOperationStream',
            monitor__pb2.MonitorRequest.SerializeToString,
            monitor__pb2.MonitorOperation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
