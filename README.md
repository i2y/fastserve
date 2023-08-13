# FastServe
FastServe is a Python library that lets you build gRPC services quickly and easily without writing protobuf files.

It automatically generates protobuf files that match the method signature of the Python object provided when starting the server.

Then, it uses the grpcio-tool to generate modules include server and client stub classes from the created protobuf files.

By dynamically generating a subclass of the server stub class and associating its methods with the original Python object's methods, it builds the gRPC server.

## Installation
Install it using your favorite package manager. Below is the method for installation using pip.

```bash
pip install fastserve
```

## Usage
Here's an example of creating a dead simple greeter service.

`greeting.py`
```python
from fastserve.core import Server, Message


class HelloRequest(Message):
    name: str


class HelloReply(Message):
    message: str


class Greeter:
    def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")


if __name__ == "__main__":
    s = Server()
    s.run(Greeter())
```


To start the server, run:
```console
$ python greeting.py
gRPC server is running...
```

In another terminal, you can call the gRPC service:
```console
$ grpcurl -plaintext -d '{"name": "World"}' localhost:50051 greeter.v1.Greeter/SayHello
{
  "message": "Hello, World!"
}
```

To list the services, use:
```console
$ grpcurl -plaintext localhost:50051 list
greeter.v1.Greeter
grpc.health.v1.Health
grpc.reflection.v1alpha.ServerReflection
```


By the way, running this will create `greeter.proto`, `greeter_pb2.py`, and `greeter_pb2_grpc.py` in the current directory.
The generated `greeter.proto` will look like this:

```proto
syntax = "proto3";

package greeter.v1;

service Greeter {
    rpc SayHello (HelloRequest) returns (HelloReply);
}

message HelloReply {
    string message = 1;
}

message HelloRequest {
    string name = 1;
}
```

You can share the generated `greeter.proto` with other services/clients written in other programming languages or Python if you want or need.


### If You Want to Use Existing Stub Modules
If you already have `greeter_pb2.py` and `greeter_pb2_grpc.py` and want to use them without generating, use `mount_using_pb2_modules` as shown below:
```python
from fastserve.core import Server, Message

import greeter_pb2_grpc, greeter_pb2


class HelloRequest(Message):
    name: str


class HelloReply(Message):
    message: str


class Greeter:
    def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")


if __name__ == "__main__":
    s = Server()
    s.mount_using_pb2_modules(greeter_pb2_grpc, greeter_pb2, Greeter())
    s.run()
```

### asyncio Version

```python
import asyncio

from fastserve.core import AsyncIOServer, Message


class HelloRequest(Message):
    name: str


class HelloReply(Message):
    message: str


class Greeter:
    async def say_hello(self, request: HelloRequest) -> HelloReply:
        return HelloReply(message=f"Hello, {request.name}!")


if __name__ == "__main__":
    s = AsyncIOServer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(s.run(Greeter()))
```

### If You Only Want to Generate protobuf Files and Stub Modules

You can execute the `fastserve.core` module to only generate the protobuf files and stub modules as follows:

```console
$ python -m fastserve.core greeting.py Greeter
```

Doing so will create `greeter.proto`, `greeter_pb2.py`, and `greeter_pb2_grpc.py` in the current directory.


### Note
- Yuo can serve multiple services by passing multiple objects to `Server.run` or calling `Server.mount` multiple times.
- You can specify the port number with `Server.set_port` method before calling `run`.
- You can set interceptors with `Server` constructor's `interceptors` argument.


## Mapping of Python Types to Protobuf Types
The following table shows the mapping of Python types to protobuf types.

| Python Type | Protobuf Type |
|:-----------:|:-------------:|
| `int` | `int32` |
| `float` | `float` |
| `str` | `string` |
| `bytes` | `bytes` |
| `bool` | `bool` |
| `List[T]` | `repeated T` |
| `Dict[str, T]` | `map<string, T>` |
| `Dict[int, T]` | `map<int32, T>` |
| `fastserve.core.Message` | `message` |

## TODO
- [ ] Support for mapping of `types.UnionType` to `oneof`
- [ ] Support for mapping of `typing.Optional` or `typing.Union[T, None]` to `oneof`
- [ ] Support for mapping of `enum.Enum` to `enum`
- [ ] Support for mapping of `datetime.datetime` to `google.protobuf.Timestamp`
- [ ] Support for mapping of `datetime.timedelta` to `google.protobuf.Duration`


## License
MIT License

## Author
Yasushi Itoh (i2y)
