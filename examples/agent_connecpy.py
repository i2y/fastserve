import asyncio

from hypercorn.asyncio import serve
from hypercorn.config import Config
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


async def main():
    app = ConnecpyASGIApp()
    app.mount(OlympicsLocationAgent())
    config = Config()
    config.bind = ["0.0.0.0:3000"]
    await serve(app, config)


if __name__ == "__main__":
    asyncio.run(main())
