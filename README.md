# AI Research & Study Assistant Agent

An autonomous AI agent built with LangChain and Google Gemini that performs multi-step reasoning — searching the web, analyzing results, and generating summarized answers through dynamic tool-calling.

## Features

- **Tool-calling**: Agent autonomously decides when to search the web using Tavily Search API
- **Persistent memory**: Maintains conversation context across multiple turns using LangGraph checkpointing
- **REST API**: FastAPI backend exposing a `/chat` endpoint for integration with any frontend
- **Web interface**: Simple chat UI built with HTML, CSS, and JavaScript

## Tech Stack

- **Language**: Python
- **LLM**: Google Gemini (via `langchain-google-genai`)
- **Agent Framework**: LangChain / LangGraph
- **Search Tool**: Tavily Search API
- **Backend**: FastAPI, Uvicorn
- **Frontend**: HTML, CSS, JavaScript

## How It Works

1. User sends a message through the chat interface
2. The agent analyzes the query and decides whether external information is needed
3. If needed, it calls the Tavily search tool to fetch real-time data
4. The LLM processes the search results and generates a coherent response
5. The conversation is stored in memory for context in future turns

## Setup Instructions

1. Clone the repository