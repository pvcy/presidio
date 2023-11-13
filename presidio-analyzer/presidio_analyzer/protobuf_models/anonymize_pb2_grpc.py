# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import anonymize_pb2 as anonymize__pb2


class AnonymizeServiceStub(object):
    """The Anonymize Service is a service that anonymizes a given the text using predefined analyzers fields and anonymize configurations.
    """

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Apply = channel.unary_unary(
                '/types.AnonymizeService/Apply',
                request_serializer=anonymize__pb2.AnonymizeRequest.SerializeToString,
                response_deserializer=anonymize__pb2.AnonymizeResponse.FromString,
                )


class AnonymizeServiceServicer(object):
    """The Anonymize Service is a service that anonymizes a given the text using predefined analyzers fields and anonymize configurations.
    """

    def Apply(self, request, context):
        """Apply method will execute on the given request and return the anonymize response with the sensitive text anonymized
        """
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_AnonymizeServiceServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'Apply': grpc.unary_unary_rpc_method_handler(
                    servicer.Apply,
                    request_deserializer=anonymize__pb2.AnonymizeRequest.FromString,
                    response_serializer=anonymize__pb2.AnonymizeResponse.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'types.AnonymizeService', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class AnonymizeService(object):
    """The Anonymize Service is a service that anonymizes a given the text using predefined analyzers fields and anonymize configurations.
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
        return grpc.experimental.unary_unary(request, target, '/types.AnonymizeService/Apply',
            anonymize__pb2.AnonymizeRequest.SerializeToString,
            anonymize__pb2.AnonymizeResponse.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)