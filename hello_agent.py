import asyncio
from autogen_agentchat.agents import AssistantAgent
from autogen_ext.models.ollama import OllamaChatCompletionClient


async def main() -> None:
    model_client = OllamaChatCompletionClient(model="llama3.2")
    agent = AssistantAgent("assistant", model_client=model_client)
    result = await agent.run(task="Say 'Hello World!'")
    print(result.messages[-1].content)
    await model_client.close()


asyncio.run(main())
