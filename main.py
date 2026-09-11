from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class ChatRequest(BaseModel):
    message: str
    thread_id: str = "default-chat"

@app.get("/")
def home():
    return {"status": "Agent is running"}

@app.post("/chat")
def chat(request: ChatRequest):
    config = {"configurable": {"thread_id": request.thread_id}}
    response = agent.invoke(
        {"messages": [{"role": "user", "content": request.message}]},
        config=config
    )
    final_content = response["messages"][-1].content
    if isinstance(final_content, list):
        final_content = " ".join([item.get("text", "") for item in final_content if isinstance(item, dict)])
    return {"reply": final_content}