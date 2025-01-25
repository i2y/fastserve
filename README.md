# PydanticRPC

**PydanticRPC** is a Python library designed to simplify the creation of gRPC services. It eliminates the need to manually write protobuf files by dynamically generating them based on Python object method signatures.

PydanticRPC leverages modern tools like `pydantic` for type validation and integrates health checks using `grpc_health.v1`. It supports both synchronous and asynchronous gRPC communication, as well as WSGI/ASGI-based gRPC-Web services.

## Key Features

- **Automatic Protobuf Generation:** Automatically creates protobuf files matching the method signatures of your Python objects.
- **Dynamic Code Generation:** Generates server and client stubs using `grpcio-tools`.
- **Health Checking:** Built-in support for gRPC health checks using `grpc_health.v1`.
- **Serevr Reflection:** Built-in support for gRPC server reflection.
- **Pydantic Integration:** Uses `pydantic` for robust type validation and serialization.
- **Asynchronous Support:** Easily create asynchronous gRPC services with `AsyncIOServer`.
- **WSGI/ASGI Support:** Create gRPC-Web services that can be run as WSGI or ASGI applications powered by `sonora`.

## Installation

Install PydanticRPC via pip:

```bash
pip install pydantic-rpc
```

## Getting Started

### Synchronous Service Example

```python
from pydanticrpc.core import Server, Message

class HelloRequest(Message):
    name: str

class HelloReply(Message):
    message: str

class Greeter:
    def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")

if __name__ == "__main__":
    server = Server()
    server.run(Greeter())
```

### Asynchronous Service Example

```python
import asyncio
from pydanticrpc.core import AsyncIOServer, Message

class HelloRequest(Message):
    name: str

class HelloReply(Message):
    message: str

class Greeter:
    async def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")

if __name__ == "__main__":
    server = AsyncIOServer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server.run(Greeter()))
```

### ASGI Application Example

```python
from pydanticrpc.core import ASGIApp, Message

class HelloRequest(Message):
    name: str

class HelloReply(Message):
    message: str

class Greeter:
    def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")

app = ASGIApp(Greeter())
```

## Advanced Features

### Multiple Services with Custom Interceptors

PydanticRPC supports defining and running multiple services in a single server:

```python
from datetime import datetime
import grpc
from grpc import ServicerContext

from pydanticrpc.core import Server, Message


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


class FooService:
    def foo(self, request: FooRequest) -> FooResponse:
        return FooResponse(name=request.name, age=request.age, d=request.d)


class MyMessage(Message):
    name: str
    age: int
    o: int | datetime


class Request(Message):
    name: str
    age: int
    d: dict[str, str]
    m: MyMessage


class Response(Message):
    name: str
    age: int
    d: dict[str, str]
    m: MyMessage | str


class BarService:
    def bar(self, req: BarRequest, ctx: ServicerContext) -> BarResponse:
        return BarResponse(names=req.names)


class CustomInterceptor(grpc.ServerInterceptor):
    def intercept_service(self, continuation, handler_call_details):
        # do something
        print(handler_call_details.method)
        return continuation(handler_call_details)


async def app(scope, receive, send):
    pass


if __name__ == "__main__":
    s = Server(10, CustomInterceptor())
    s.run(
        FooService(),
        BarService(),
    )
```

### [TODO] Custom Health Check
TODO

### Protobuf file generation
You can generate protobuf files for a given module and a specified class using `core.py`:

```bash
python core.py a_module.py aClass
```

## [WIP] Contributing

Contributions are welcome! To get started:

1. Fork the repository.
2. Create a new branch for your feature (`git checkout -b feature-name`).
3. Commit your changes (`git commit -m 'Add feature'`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.

[WIP] Please make sure to follow the [Contribution Guidelines](CONTRIBUTING.md).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
