# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import datasink_pb2 as datasink__pb2
import template_pb2 as template__pb2


class DatasinkServiceStub(object):
    """The data sink service represents the service for writing the results of the analyzing and anonymizng service.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Apply = channel.unary_unary(
                '/types.DatasinkService/Apply',
                request_serializer=datasink__pb2.DatasinkRequest.SerializeToString,
                response_deserializer=datasink__pb2.DatasinkResponse.FromString,
                )
        self.Init = channel.unary_unary(
                '/types.DatasinkService/Init',
                request_serializer=template__pb2.DatasinkTemplate.SerializeToString,
                response_deserializer=datasink__pb2.DatasinkResponse.FromString,
                )
        self.Completion = channel.unary_unary(
                '/types.DatasinkService/Completion',
                request_serializer=datasink__pb2.CompletionMessage.SerializeToString,
                response_deserializer=datasink__pb2.DatasinkResponse.FromString,
                )


class DatasinkServiceServicer(object):
    """The data sink service represents the service for writing the results of the analyzing and anonymizng service.
    """

    def Apply(self, request, context):
        """Apply method will execute on the given request and return whether the result where written successfully to the destination
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Init(self, request, context):
        """Init the data sink service with the provided data sink template
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')

    def Completion(self, request, context):
        """Completion method for indicating that the scanning job is done
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_DatasinkServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Apply': grpc.unary_unary_rpc_method_handler(
                    servicer.Apply,
                    request_deserializer=datasink__pb2.DatasinkRequest.FromString,
                    response_serializer=datasink__pb2.DatasinkResponse.SerializeToString,
            ),
            'Init': grpc.unary_unary_rpc_method_handler(
                    servicer.Init,
                    request_deserializer=template__pb2.DatasinkTemplate.FromString,
                    response_serializer=datasink__pb2.DatasinkResponse.SerializeToString,
            ),
            'Completion': grpc.unary_unary_rpc_method_handler(
                    servicer.Completion,
                    request_deserializer=datasink__pb2.CompletionMessage.FromString,
                    response_serializer=datasink__pb2.DatasinkResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'types.DatasinkService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class DatasinkService(object):
    """The data sink service represents the service for writing the results of the analyzing and anonymizng service.
    """

    @staticmethod
    def Apply(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/types.DatasinkService/Apply',
            datasink__pb2.DatasinkRequest.SerializeToString,
            datasink__pb2.DatasinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Init(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/types.DatasinkService/Init',
            template__pb2.DatasinkTemplate.SerializeToString,
            datasink__pb2.DatasinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)

    @staticmethod
    def Completion(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/types.DatasinkService/Completion',
            datasink__pb2.CompletionMessage.SerializeToString,
            datasink__pb2.DatasinkResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
