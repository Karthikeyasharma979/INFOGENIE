from smolagents import ToolCallingAgent,DuckDuckGoSearchTool,HfApiModel,LiteLLMModel
from Summarizer import summarize
from dotenv import load_dotenv
load_dotenv() 


def process_ai_analysis(message):
    model = HfApiModel()
    # system = "Use summarize_tool only when explicitly asked for summarization."
    agent = ToolCallingAgent(tools=[DuckDuckGoSearchTool(),summarize()],model=model)
    res = agent.run(message)
    # print(agent.reasoning)
    return res

# process_ai_analysis()

