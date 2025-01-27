import asyncio

from pydantic import field_validator
from pydantic_ai import Agent
from pydantic_rpc import AsyncIOServer, Message


# `Message` is just a pydantic BaseModel alias
class CityLocation(Message):
    city: str
    country: str


class Olympics(Message):
    year: int

    def prompt(self):
        return f"Where were the Olympics held in {self.year}?"

    @field_validator("year")
    def validate_year(cls, value):
        if value < 1896:
            raise ValueError("The first modern Olympics was held in 1896.")

        if value % 4 != 0:
            raise ValueError("The Olympics are held every 4 years.")

        return value


class OlympicsLocationAgent:
    def __init__(self):
        self._agent = Agent("ollama:llama3.2", result_type=CityLocation)

    async def ask(self, req: Olympics) -> CityLocation:
        result = await self._agent.run(req.prompt())
        return result.data


if __name__ == "__main__":
    s = AsyncIOServer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(s.run(OlympicsLocationAgent()))
