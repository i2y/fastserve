from pydantic_rpc import ASGIApp, Message


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

    async def say_hello(self, request: HelloRequest) -> HelloReply:
        """Says hello to the user.

        Args:
            request (HelloRequest): The request message.

        Returns:
            HelloReply: The reply message.
        """
        return HelloReply(message=f"Hello, {request.name}!")


async def app(scope, receive, send):
    """ASGI application.

    Args:
        scope (dict): The ASGI scope.
        receive (callable): The receive function.
        send (callable): The send function.
    """
    pass


app = ASGIApp(app)
app.mount_objs(Greeter())
