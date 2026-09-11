from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_tavily import TavilySearch
from langchain.agents import create_agent
from langgraph.checkpoint.memory import InMemorySaver

load_dotenv()

llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

search_tool = TavilySearch(max_results=3)

tools = [search_tool]

memory = InMemorySaver()

agent = create_agent(llm, tools, checkpointer=memory)

config = {"configurable": {"thread_id": "chat-1"}}

while True:
    user_input = input("\nAap: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    response = agent.invoke(
        {"messages": [{"role": "user", "content": user_input}]},
        config=config
    )
    print("\nAgent:", response["messages"][-1].content)