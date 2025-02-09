# -*- coding: utf-8 -*-
# Generated by https://github.com/i2y/connecpy/protoc-gen-connecpy.  DO NOT EDIT!
# source: asyncechoservice.proto

from typing import Any, Protocol, Union

import httpx

from connecpy.async_client import AsyncConnecpyClient
from connecpy.base import Endpoint
from connecpy.server import ConnecpyServer
from connecpy.client import ConnecpyClient
from connecpy.context import ClientContext, ServiceContext

import asyncechoservice_pb2 as _pb2

from google.protobuf import symbol_database

_sym_db = symbol_database.Default()


class AsyncEchoService(Protocol):
    async def Echo(
        self, req: _pb2.EchoRequest, ctx: ServiceContext
    ) -> _pb2.EchoResponse: ...


class AsyncEchoServiceServer(ConnecpyServer):
    def __init__(self, *, service: AsyncEchoService, server_path_prefix=""):
        super().__init__()
        self._prefix = f"{server_path_prefix}/asyncecho.v1.AsyncEchoService"
        self._endpoints = {
            "Echo": Endpoint[_pb2.EchoRequest, _pb2.EchoResponse](
                service_name="AsyncEchoService",
                name="Echo",
                function=getattr(service, "Echo"),
                input=_pb2.EchoRequest,
                output=_pb2.EchoResponse,
            ),
        }

    def serviceName(self):
        return "asyncecho.v1.AsyncEchoService"


class AsyncEchoServiceSync(Protocol):
    def Echo(self, req: _pb2.EchoRequest, ctx: ServiceContext) -> _pb2.EchoResponse: ...


class AsyncEchoServiceServerSync(ConnecpyServer):
    def __init__(self, *, service: AsyncEchoServiceSync, server_path_prefix=""):
        super().__init__()
        self._prefix = f"{server_path_prefix}/asyncecho.v1.AsyncEchoService"
        self._endpoints = {
            "Echo": Endpoint[_pb2.EchoRequest, _pb2.EchoResponse](
                service_name="AsyncEchoService",
                name="Echo",
                function=getattr(service, "Echo"),
                input=_pb2.EchoRequest,
                output=_pb2.EchoResponse,
            ),
        }

    def serviceName(self):
        return "asyncecho.v1.AsyncEchoService"


class AsyncEchoServiceClient(ConnecpyClient):
    def Echo(
        self,
        *,
        request: _pb2.EchoRequest,
        ctx: ClientContext,
        server_path_prefix: str = "",
        **kwargs,
    ) -> _pb2.EchoResponse:
        return self._make_request(
            url=f"{server_path_prefix}/asyncecho.v1.AsyncEchoService/Echo",
            ctx=ctx,
            request=request,
            response_obj=_pb2.EchoResponse,
            **kwargs,
        )


class AsyncAsyncEchoServiceClient(AsyncConnecpyClient):
    async def Echo(
        self,
        *,
        request: _pb2.EchoRequest,
        ctx: ClientContext,
        server_path_prefix: str = "",
        session: Union[httpx.AsyncClient, None] = None,
        **kwargs,
    ) -> _pb2.EchoResponse:
        return await self._make_request(
            url=f"{server_path_prefix}/asyncecho.v1.AsyncEchoService/Echo",
            ctx=ctx,
            request=request,
            response_obj=_pb2.EchoResponse,
            session=session,
            **kwargs,
        )
