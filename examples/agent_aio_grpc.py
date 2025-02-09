import asyncio
from typing import Annotated, AsyncIterator

from openai import AsyncOpenAI
from pydantic import Field
from pydantic_ai import Agent
from pydantic_ai.models.openai import OpenAIModel
from pydantic_rpc import AsyncIOServer, Message


# `Message` is just a pydantic BaseModel alias
class CityLocation(Message):
    city: Annotated[str, Field(description="The city where the Olympics were held")]
    country: Annotated[
        str, Field(description="The country where the Olympics were held")
    ]


class OlympicsQuery(Message):
    year: Annotated[int, Field(description="The year of the Olympics", ge=1896)]

    def prompt(self):
        return f"Where were the Olympics held in {self.year}?"


class OlympicsDurationQuery(Message):
    start: Annotated[int, Field(description="The start year of the Olympics", ge=1896)]
    end: Annotated[int, Field(description="The end year of the Olympics", ge=1896)]

    def prompt(self):
        return f"From {self.start} to {self.end}, how many Olympics were held? Please provide the list of countries and cities."


class StreamingResult(Message):
    answer: Annotated[str, Field(description="The answer to the query")]


class OlympicsAgent:
    def __init__(self):
        client = AsyncOpenAI(
            base_url="http://localhost:11434/v1",
            api_key="ollama_api_key",
        )
        ollama_model = OpenAIModel(
            model_name="llama3.2",
            openai_client=client,
        )
        self._agent = Agent(ollama_model)

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
