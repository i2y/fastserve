# import grpc
# from greeter_pb2 import HelloRequest
# from greeter_pb2_grpc import GreeterStub


# def run():
#     with grpc.insecure_channel("localhost:50051") as channel:
#         stub = GreeterStub(channel)
#         response = stub.SayHello(HelloRequest(name="World"))
#         print(response.message)


# if __name__ == "__main__":
#     run()

from connecpy.context import ClientContext
from connecpy.exceptions import ConnecpyServerException

import greeter_connecpy
import greeter_pb2


server_url = "http://localhost:3000"
timeout_s = 5


def main():
    client = greeter_connecpy.GreeterClient(server_url, timeout=timeout_s)

    try:
        response = client.SayHello(
            ctx=ClientContext(),
            request=greeter_pb2.HelloRequest(name="World"),
        )
        print(response)
    except ConnecpyServerException as e:
        print(e.code, e.message, e.to_dict())


if __name__ == "__main__":
    main()
