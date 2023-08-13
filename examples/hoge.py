import grpc
from grpc import ServicerContext

from fastserve.core import Server, Message


class FooRequest(Message):
    name: str
    age: int
    d: dict[str, str]


class FooResponse(Message):
    name: str
    age: int
    d: dict[str, str]


class BarRequest(Message):
    names: list[str]


class BarResponse(Message):
    names: list[str]


class HogeService:
    def foo(self, request: FooRequest) -> FooResponse:
        return FooResponse(name=request.name, age=request.age, d=request.d)

    def bar(self, req: BarRequest, ctx: ServicerContext) -> BarResponse:
        return BarResponse(names=req.names)


class MyMessage(Message):
    name: str
    age: int


class Request(Message):
    name: str
    age: int
    d: dict[str, str]
    m: MyMessage


class Response(Message):
    name: str
    age: int
    d: dict[str, str]
    m: MyMessage


class FugaService:
    def foo(self, request: Request) -> Response:
        return Response(name=request.name, age=request.age, d=request.d, m=request.m)


class CustomInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        # ここで何かの処理を行う
        print(handler_call_details.method)
        return continuation(handler_call_details)


if __name__ == "__main__":
    s = Server(10, CustomInterceptor())
    # s.set_package_name("hoge.v1")
    s.run(
        HogeService(),
        FugaService(),
    )
