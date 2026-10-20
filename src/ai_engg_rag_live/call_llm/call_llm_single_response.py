import asyncio
import os

from dotenv import load_dotenv
from ollama import AsyncClient

load_dotenv()


class ChatService:

    def __init__(self):
        api_key = os.environ["OLLAMA_API_KEY"]
        self.model = os.getenv("OLLAMA_MODEL", "kimi-k2.7-code:cloud")

        self.client = AsyncClient(
            host="https://ollama.com",
            headers={"Authorization": f"Bearer {api_key}"}
        )

    async def ask(self, question: str) -> str:
        response = await self.client.chat(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": question,
                }
            ]
        )

        return response.message.content


async def main():
    chat_service = ChatService()
    query = input("Query: ")
    answer = await chat_service.ask(query)
    print(answer)


if __name__ == "__main__":
    asyncio.run(main())

