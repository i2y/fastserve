import grpc
from greeter_pb2 import HelloRequest
from greeter_pb2_grpc import GreeterStub


def run():
    with grpc.insecure_channel("localhost:50051") as channel:
        stub = GreeterStub(channel)
        response = stub.SayHello(HelloRequest(name="World"))
        print(response.message)


if __name__ == "__main__":
    run()
