# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

from google.protobuf import empty_pb2 as google_dot_protobuf_dot_empty__pb2
import meteoServer_pb2 as meteoServer__pb2


class LBServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.AddAirData = channel.unary_unary(
                '/LBService/AddAirData',
                request_serializer=meteoServer__pb2.RawMeteoData.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.AddPollData = channel.unary_unary(
                '/LBService/AddPollData',
                request_serializer=meteoServer__pb2.RawPollutionData.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class LBServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def AddAirData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def AddPollData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_LBServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'AddAirData': grpc.unary_unary_rpc_method_handler(
                    servicer.AddAirData,
                    request_deserializer=meteoServer__pb2.RawMeteoData.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'AddPollData': grpc.unary_unary_rpc_method_handler(
                    servicer.AddPollData,
                    request_deserializer=meteoServer__pb2.RawPollutionData.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'LBService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class LBService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def AddAirData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LBService/AddAirData',
            meteoServer__pb2.RawMeteoData.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def AddPollData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/LBService/AddPollData',
            meteoServer__pb2.RawPollutionData.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)


class MeteoServiceStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.ProcessMeteoData = channel.unary_unary(
                '/MeteoService/ProcessMeteoData',
                request_serializer=meteoServer__pb2.RawMeteoData.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )
        self.ProcessPollData = channel.unary_unary(
                '/MeteoService/ProcessPollData',
                request_serializer=meteoServer__pb2.RawPollutionData.SerializeToString,
                response_deserializer=google_dot_protobuf_dot_empty__pb2.Empty.FromString,
                )


class MeteoServiceServicer(object):
    """Missing associated documentation comment in .proto file."""

    def ProcessMeteoData(self, request, context):
        """rpc GetInsults (google.protobuf.Empty) returns (Insults) {}
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def ProcessPollData(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_MeteoServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'ProcessMeteoData': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessMeteoData,
                    request_deserializer=meteoServer__pb2.RawMeteoData.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
            'ProcessPollData': grpc.unary_unary_rpc_method_handler(
                    servicer.ProcessPollData,
                    request_deserializer=meteoServer__pb2.RawPollutionData.FromString,
                    response_serializer=google_dot_protobuf_dot_empty__pb2.Empty.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'MeteoService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class MeteoService(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def ProcessMeteoData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MeteoService/ProcessMeteoData',
            meteoServer__pb2.RawMeteoData.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def ProcessPollData(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/MeteoService/ProcessPollData',
            meteoServer__pb2.RawPollutionData.SerializeToString,
            google_dot_protobuf_dot_empty__pb2.Empty.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
