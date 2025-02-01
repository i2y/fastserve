import sonora.client

from greeter_pb2_grpc import GreeterStub
from greeter_pb2 import HelloRequest

with sonora.client.insecure_web_channel("http://localhost:3000") as channel:
    stub = GreeterStub(channel)
    print(stub.SayHello(HelloRequest(name="world")))
