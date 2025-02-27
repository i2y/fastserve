# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""

import grpc
import warnings

import olympicsagent_pb2 as olympicsagent__pb2

GRPC_GENERATED_VERSION = "1.70.0"
GRPC_VERSION = grpc.__version__
_version_not_supported = False

try:
    from grpc._utilities import first_version_is_lower

    _version_not_supported = first_version_is_lower(
        GRPC_VERSION, GRPC_GENERATED_VERSION
    )
except ImportError:
    _version_not_supported = True

if _version_not_supported:
    raise RuntimeError(
        f"The grpc package installed is at version {GRPC_VERSION},"
        + f" but the generated code in olympicsagent_pb2_grpc.py depends on"
        + f" grpcio>={GRPC_GENERATED_VERSION}."
        + f" Please upgrade your grpc module to grpcio>={GRPC_GENERATED_VERSION}"
        + f" or downgrade your generated code using grpcio-tools<={GRPC_VERSION}."
    )


class OlympicsAgentStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.Ask = channel.unary_unary(
            "/olympicsagent.v1.OlympicsAgent/Ask",
            request_serializer=olympicsagent__pb2.OlympicsQuery.SerializeToString,
            response_deserializer=olympicsagent__pb2.CityLocation.FromString,
            _registered_method=True,
        )
        self.AskStream = channel.unary_stream(
            "/olympicsagent.v1.OlympicsAgent/AskStream",
            request_serializer=olympicsagent__pb2.OlympicsDurationQuery.SerializeToString,
            response_deserializer=olympicsagent__pb2.StreamingResult.FromString,
            _registered_method=True,
        )


class OlympicsAgentServicer(object):
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


def add_OlympicsAgentServicer_to_server(servicer, server):
    rpc_method_handlers = {
        "Ask": grpc.unary_unary_rpc_method_handler(
            servicer.Ask,
            request_deserializer=olympicsagent__pb2.OlympicsQuery.FromString,
            response_serializer=olympicsagent__pb2.CityLocation.SerializeToString,
        ),
        "AskStream": grpc.unary_stream_rpc_method_handler(
            servicer.AskStream,
            request_deserializer=olympicsagent__pb2.OlympicsDurationQuery.FromString,
            response_serializer=olympicsagent__pb2.StreamingResult.SerializeToString,
        ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
        "olympicsagent.v1.OlympicsAgent", rpc_method_handlers
    )
    server.add_generic_rpc_handlers((generic_handler,))
    server.add_registered_method_handlers(
        "olympicsagent.v1.OlympicsAgent", rpc_method_handlers
    )


# This class is part of an EXPERIMENTAL API.
class OlympicsAgent(object):
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
            "/olympicsagent.v1.OlympicsAgent/Ask",
            olympicsagent__pb2.OlympicsQuery.SerializeToString,
            olympicsagent__pb2.CityLocation.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
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
            "/olympicsagent.v1.OlympicsAgent/AskStream",
            olympicsagent__pb2.OlympicsDurationQuery.SerializeToString,
            olympicsagent__pb2.StreamingResult.FromString,
            options,
            channel_credentials,
            insecure,
            call_credentials,
            compression,
            wait_for_ready,
            timeout,
            metadata,
            _registered_method=True,
        )
