from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console

team = RoundRobinGroupChat(
    [agent_a, agent_b],
    termination_condition=TextMentionTermination("TERMINATE"),
)
await Console(team.run_stream(task="Research and summarize X"))