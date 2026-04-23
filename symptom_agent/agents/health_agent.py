from langchain.agents import create_agent
from langchain.messages import HumanMessage

from langchain_ollama import ChatOllama
from langchain_mcp_adapters.client import MultiServerMCPClient
from dotenv import load_dotenv
from langgraph.checkpoint.postgres.aio import AsyncPostgresSaver
import os
from .prompts import SYSTEM_PROMPT
from symptom_agent.db.db_operations import save_message

load_dotenv()

DB_URL = os.environ.get("POSTGRES_DATABASE")


async def get_mcp_tools():
    client = MultiServerMCPClient(
        {
            "healthcare": {
                "command": "npx",
                "args": ["-y", "@easysolutions906/mcp-healthcare"],
                "transport": "stdio",
            }
        }
    )

    tools = await client.get_tools()

    return tools


async def chat_agent(query: str) -> str:
    tools = await get_mcp_tools()
    async with AsyncPostgresSaver.from_conn_string(DB_URL) as conn:
        await conn.setup()
        agent = create_agent(
            model=ChatOllama(model="minimax-m2.7:cloud"),
            system_prompt=SYSTEM_PROMPT,
            tools=tools,
            checkpointer=conn,
        )
        response = await agent.ainvoke(
            {"messages": [HumanMessage(content=query)]},
            config={"configurable": {"thread_id": "1"}},
        )
        save_message(
            thread_id="1", query=query, ai_res=response["messages"][-1].content
        )
        return response["messages"][-1].content
