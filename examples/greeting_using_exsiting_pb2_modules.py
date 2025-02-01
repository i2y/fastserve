from pydantic_rpc import Server, Message

import greeter_pb2_grpc
import greeter_pb2


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
