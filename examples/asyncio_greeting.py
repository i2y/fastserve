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
