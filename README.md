# 🚀 PydanticRPC

**PydanticRPC** is a Python library that enables you to rapidly expose [Pydantic](https://docs.pydantic.dev/) models via [gRPC](https://grpc.io/)/[Connect RPC](https://connectrpc.com/docs/protocol/) services without writing any protobuf files. Instead, it automatically generates protobuf files on the fly from the method signatures of your Python objects and the type signatures of your Pydantic models.


Below is an example of a simple gRPC service that exposes a [PydanticAI](https://ai.pydantic.dev/) agent:

```python
import asyncio

from pydantic_ai import Agent
from pydantic_rpc import AsyncIOServer, Message


# `Message` is just an alias for Pydantic's `BaseModel` class.
class CityLocation(Message):
    city: str
    country: str


class Olympics(Message):
    year: int

    def prompt(self):
        return f"Where were the Olympics held in {self.year}?"


class OlympicsLocationAgent:
    def __init__(self):
        self._agent = Agent("ollama:llama3.2", result_type=CityLocation)

    async def ask(self, req: Olympics) -> CityLocation:
        result = await self._agent.run(req.prompt())
        return result.data


if __name__ == "__main__":
    s = AsyncIOServer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(s.run(OlympicsLocationAgent()))
```

And here is an example of a simple Connect RPC service that exposes the same agent as an ASGI application:

```python
import asyncio

from pydantic_ai import Agent
from pydantic_rpc import ConnecpyASGIApp, Message


class CityLocation(Message):
    city: str
    country: str


class Olympics(Message):
    year: int

    def prompt(self):
        return f"Where were the Olympics held in {self.year}?"


class OlympicsLocationAgent:
    def __init__(self):
        self._agent = Agent("ollama:llama3.2", result_type=CityLocation)

    async def ask(self, req: Olympics) -> CityLocation:
        result = await self._agent.run(req.prompt())
        return result.data

app = ConnecpyASGIApp()
app.mount(OlympicsLocationAgent())

```


## 💡 Key Features

- 🔄 **Automatic Protobuf Generation:** Automatically creates protobuf files matching the method signatures of your Python objects.
- ⚙️ **Dynamic Code Generation:** Generates server and client stubs using `grpcio-tools`.
- ✅ **Pydantic Integration:** Uses `pydantic` for robust type validation and serialization.
- 📄 **Pprotobuf File Export:** Exports the generated protobuf files for use in other languages.
- **For gRPC:**
  - 💚 **Health Checking:** Built-in support for gRPC health checks using `grpc_health.v1`.
  - 🔎 **Server Reflection:** Built-in support for gRPC server reflection.
  - ⚡ **Asynchronous Support:** Easily create asynchronous gRPC services with `AsyncIOServer`.
- **For gRPC-Web:**
  - 🌐 **WSGI/ASGI Support:** Create gRPC-Web services that can run as WSGI or ASGI applications powered by `Sonora`.
- **For Connect-RPC:**
  - 🌐 **Connecpy Support:** Partially supports Connect-RPC via `Connecpy`.

## 📦 Installation

Install PydanticRPC via pip:

```bash
pip install pydantic-rpc
```

## 🚀 Getting Started

### 🔧 Synchronous Service Example

```python
from pydantic_rpc import Server, Message

class HelloRequest(Message):
    name: str

class HelloReply(Message):
    message: str

class Greeter:
    # Define methods that accepts a request and returns a response.
    def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")

if __name__ == "__main__":
    server = Server()
    server.run(Greeter())
```

### ⚙️ Asynchronous Service Example

```python
import asyncio

from pydantic_rpc import AsyncIOServer, Message


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

### 🌐 ASGI Application Example

```python
from pydantic_rpc import ASGIApp, Message

class HelloRequest(Message):
    name: str

class HelloReply(Message):
    message: str

class Greeter:
    def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")


async def app(scope, receive, send):
    """ASGI application.

    Args:
        scope (dict): The ASGI scope.
        receive (callable): The receive function.
        send (callable): The send function.
    """
    pass

# Please note that `app` is any ASGI application, such as FastAPI or Starlette.

app = ASGIApp(app)
app.mount(Greeter())
```

### 🌐 WSGI Application Example

```python
from pydantic_rpc import WSGIApp, Message

class HelloRequest(Message):
    name: str

class HelloReply(Message):
    message: str

class Greeter:
    def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")

def app(environ, start_response):
    """WSGI application.

    Args:
        environ (dict): The WSGI environment.
        start_response (callable): The start_response function.
    """
    pass

# Please note that `app` is any WSGI application, such as Flask or Django.

app = WSGIApp(app)
app.mount(Greeter())
```

### 🏆 Connecpy (Connect-RPC) Example

PydanticRPC also partially supports Connect-RPC via connecpy. Check out “greeting_connecpy.py” for an example:

```bash
uv run greeting_connecpy.py
```

This will launch a Connecpy-based ASGI application that uses the same Pydantic models to serve Connect-RPC requests.

> [!NOTE]
> Please install `protoc-gen-connecpy` to run the Connecpy example.
>
> 1. Install Go.
>     - Please follow the instruction described in https://go.dev/doc/install.
> 2. Install `protoc-gen-connecpy`:
>     ```bash
>     go install github.com/connecpy/protoc-gen-connecpy@latest
>     ```

## ♻️ Skipping Protobuf Generation
By default, PydanticRPC generates .proto files and code at runtime. If you wish to skip the code-generation step (for example, in production environment), set the environment variable below:

```bash
export PYDANTIC_RPC_SKIP_GENERATION=true
```

When this variable is set to "true", PydanticRPC will load existing pre-generated modules rather than generating them on the fly.

## 💎 Advanced Features

### 🌊 Response Streaming
PydanticRPC supports streaming for responses in asynchronous gRPC and gRPC-Web services only.

Please see the sample code below:

```python
import asyncio
from typing import Annotated, AsyncIterator

from pydantic import Field
from pydantic_ai import Agent
from pydantic_rpc import AsyncIOServer, Message


# `Message` is just a pydantic BaseModel alias
class CityLocation(Message):
    city: Annotated[str, Field(description="The city where the Olympics were held")]
    country: Annotated[
        str, Field(description="The country where the Olympics were held")
    ]


class OlympicsQuery(Message):
    year: Annotated[int, Field(description="The year of the Olympics", ge=1896)]

    def prompt(self):
        return f"Where were the Olympics held in {self.year}?"


class OlympicsDurationQuery(Message):
    start: Annotated[int, Field(description="The start year of the Olympics", ge=1896)]
    end: Annotated[int, Field(description="The end year of the Olympics", ge=1896)]

    def prompt(self):
        return f"From {self.start} to {self.end}, how many Olympics were held? Please provide the list of countries and cities."


class StreamingResult(Message):
    answer: Annotated[str, Field(description="The answer to the query")]


class OlympicsAgent:
    def __init__(self):
        self._agent = Agent("ollama:llama3.2")

    async def ask(self, req: OlympicsQuery) -> CityLocation:
        result = await self._agent.run(req.prompt(), result_type=CityLocation)
        return result.data

    async def ask_stream(
        self, req: OlympicsDurationQuery
    ) -> AsyncIterator[StreamingResult]:
        async with self._agent.run_stream(req.prompt(), result_type=str) as result:
            async for data in result.stream_text(delta=True):
                yield StreamingResult(answer=data)


if __name__ == "__main__":
    s = AsyncIOServer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(s.run(OlympicsAgent()))
```

### 🔗 Multiple Services with Custom Interceptors

PydanticRPC supports defining and running multiple services in a single server:

```python
from datetime import datetime
import grpc
from grpc import ServicerContext

from pydantic_rpc import Server, Message


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

### 🩺 [TODO] Custom Health Check

TODO

### 🗄️ Protobuf file generation

You can generate protobuf files for a given module and a specified class using `core.py`:

```bash
python core.py a_module.py aClass
```

Using this generated proto file and tools as `protoc`, `buf` and `BSR`, you could generate code for any desired language other than Python.

## 📖 Data Type Mapping

| Python Type                    | Protobuf Type             |
|--------------------------------|---------------------------|
| str                            | string                    |
| bytes                          | bytes                     |
| bool                           | bool                      |
| int                            | int32                     |
| float                          | float, double             |
| list[T], tuple[T]              | repeated T                |
| dict[K, V]                     | map<K, V>                 |
| datetime.datetime              | google.protobuf.Timestamp |
| datetime.timedelta             | google.protobuf.Duration  |
| typing.Union[A, B]             | oneof A, B                |
| subclass of enum.Enum          | enum                      |
| subclass of pydantic.BaseModel | message                   |


## TODO
- [ ] Streaming Support
  - [x] unary-stream
  - [ ] stream-unary
  - [ ] stream-stream
- [ ] Betterproto Support
- [ ] Sonora-connect Support
- [ ] Custom Health Check Support
- [ ] Add more examples
- [ ] Add tests

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
