import asyncio
from typing import AsyncIterator

from pydantic import field_validator
from pydantic_ai import Agent
from pydantic_rpc import AsyncIOServer, Message


# `Message` is just a pydantic BaseModel alias
class CityLocation(Message):
    city: str
    country: str


class OlympicsQuery(Message):
    year: int

    def prompt(self):
        return f"Where were the Olympics held in {self.year}?"

    @field_validator("year")
    def validate_year(cls, value):
        if value < 1896:
            raise ValueError("The first modern Olympics was held in 1896.")

        return value


class OlympicsDurationQuery(Message):
    start: int
    end: int

    def prompt(self):
        return f"From {self.start} to {self.end}, how many Olympics were held? Please provide the list of countries and cities."

    @field_validator("start")
    def validate_start(cls, value):
        if value < 1896:
            raise ValueError("The first modern Olympics was held in 1896.")

        return value

    @field_validator("end")
    def validate_end(cls, value):
        if value < 1896:
            raise ValueError("The first modern Olympics was held in 1896.")

        return value


class StreamingResult(Message):
    answer: str


class OlympicsAgent:
    def __init__(self):
        self._agent = Agent("ollama:llama3.2")

    async def ask(self, req: OlympicsQuery) -> CityLocation:
        result = await self._agent.run(req.prompt(), result_type=CityLocation)
        return result.data

    async def ask_stream(
        self, req: OlympicsDurationQuery
    ) -> AsyncIterator[StreamingResult]:
        async with self._agent.run_stream(req.prompt(), result_type=str) as result:
            async for data in result.stream_text(delta=True):
                yield StreamingResult(answer=data)


if __name__ == "__main__":
    s = AsyncIOServer()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(s.run(OlympicsAgent()))
