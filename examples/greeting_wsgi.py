from wsgiref.simple_server import make_server

from pydantic_rpc import WSGIApp, Message


class HelloRequest(Message):
    """Request message.
    This is a simple example of a request message.

    Attributes:
        name (str): The name of the person to greet.
    """

    name: str


class HelloReply(Message):
    """Reply message.
    This is a simple example of a reply message.

    Attributes:
        message (str): The message to be sent.
    """

    message: str


class Greeter:
    """Greeter service.
    This is a simple example of a service that greets you.
    """

    def say_hello(self, request: HelloRequest) -> HelloReply:
        """Says hello to the user.

        Args:
            request (HelloRequest): The request message.

        Returns:
            HelloReply: The reply message.
        """
        return HelloReply(message=f"Hello, {request.name}!")


def app(environ, start_response):
    """WSGI app.
    This is a simple example of a WSGI app.

    Args:
        environ (dict): The WSGI environ.
        start_response (callable): The WSGI start_response.
    """
    start_response("200 OK", [("Content-Type", "text/plain")])
    return [b"Hello, world!"]


app = WSGIApp(app)
app.mount_objs(Greeter())

if __name__ == "__main__":
    with make_server("", 3000, app) as httpd:
        print("Serving on port 3000...")
        httpd.serve_forever()
