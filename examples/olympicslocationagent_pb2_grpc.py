# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc

import olympicslocationagent_pb2 as olympicslocationagent__pb2


class OlympicsLocationAgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ask = channel.unary_unary(
            "/olympicslocationagent.v1.OlympicsLocationAgent/Ask",
            request_serializer=olympicslocationagent__pb2.Olympics.SerializeToString,
            response_deserializer=olympicslocationagent__pb2.CityLocation.FromString,
        )
        self.AskStream = channel.unary_stream(
            "/olympicslocationagent.v1.OlympicsLocationAgent/AskStream",
            request_serializer=olympicslocationagent__pb2.Duration.SerializeToString,
            response_deserializer=olympicslocationagent__pb2.Result.FromString,
        )


class OlympicsLocationAgentServicer(object):
    """Missing associated documentation comment in .proto file."""

    def Ask(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")

    def AskStream(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details("Method not implemented!")
        raise NotImplementedError("Method not implemented!")


def add_OlympicsLocationAgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Ask": grpc.unary_unary_rpc_method_handler(
            servicer.Ask,
            request_deserializer=olympicslocationagent__pb2.Olympics.FromString,
            response_serializer=olympicslocationagent__pb2.CityLocation.SerializeToString,
        ),
        "AskStream": grpc.unary_stream_rpc_method_handler(
            servicer.AskStream,
            request_deserializer=olympicslocationagent__pb2.Duration.FromString,
            response_serializer=olympicslocationagent__pb2.Result.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "olympicslocationagent.v1.OlympicsLocationAgent", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))


# This class is part of an EXPERIMENTAL API.
class OlympicsLocationAgent(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def Ask(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_unary(
            request,
            target,
            "/olympicslocationagent.v1.OlympicsLocationAgent/Ask",
            olympicslocationagent__pb2.Olympics.SerializeToString,
            olympicslocationagent__pb2.CityLocation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )

    @staticmethod
    def AskStream(
        request,
        target,
        options=(),
        channel_credentials=None,
        call_credentials=None,
        insecure=False,
        compression=None,
        wait_for_ready=None,
        timeout=None,
        metadata=None,
    ):
        return grpc.experimental.unary_stream(
            request,
            target,
            "/olympicslocationagent.v1.OlympicsLocationAgent/AskStream",
            olympicslocationagent__pb2.Duration.SerializeToString,
            olympicslocationagent__pb2.Result.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
        )
