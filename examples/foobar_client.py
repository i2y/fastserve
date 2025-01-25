import grpc
from fooservice_pb2 import FooRequest
from fooservice_pb2_grpc import FooServiceStub

from barservice_pb2 import BarRequest
from barservice_pb2_grpc import BarServiceStub


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = FooServiceStub(channel)
        response = stub.Foo(FooRequest(name="World", age=42, d={"a": "b"}))
        print(response.name, response.age, response.d)
        stub = BarServiceStub(channel)
        response = stub.Bar(BarRequest(names=["a", "b", "c"]))
        print(response.names)


if __name__ == "__main__":
    run()
