import asyncio
from autogen_agentchat.agents import AssistantAgent
# We still use the OpenAI client because Ollama provides an OpenAI-compatible API
from autogen_ext.models.openai import OpenAIChatCompletionClient
from autogen_ext.models.ollama import OllamaChatCompletionClient

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console

async def main():
    # Configure the client to talk to your local machine instead of OpenAI's servers
    local_client = OllamaChatCompletionClient(model="llama3.2:latest")

    # Now you can instantiate your agents using the local client
    agent_a = AssistantAgent(
        name="agent_a",
        model_client=local_client,
        system_message="You are a helpful research assistant."
    )
    
    agent_b = AssistantAgent(
        name="agent_b",
        model_client=local_client,
        system_message="You are a critical summary editor. Reply with TERMINATE when done."
    )

    team = RoundRobinGroupChat(
        [agent_a, agent_b],
        termination_condition=TextMentionTermination("TERMINATE"),
    )
    
    await Console(team.run_stream(task="Research and summarize X"))

if __name__ == "__main__":
    asyncio.run(main())
