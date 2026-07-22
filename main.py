from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage
)
from tools.db_tool import query_executor
from tools.input_tool import take_user_input
import os
from dotenv import load_dotenv

load_dotenv()

llm=ChatOpenAI(
    base_url=os.getenv("base_url"),
    api_key=os.getenv("api"),
    model=os.getenv("model")
)

context=[
    SystemMessage(content="""
You are a My sql ReAct agent , your task is to generate the mysql queries accrding to the users nees
""")
]

tool_binded_llm=llm.bind_tools(
    [
        query_executor,
        take_user_input
    ]
)
while True:
    user_input=input("Query: ")
    context.append(HumanMessage(content=user_input))

    response=tool_binded_llm.invoke(context)
    context.append(AIMessage(response.content))
    
    if not response.content:
        
        print(response.tool_calls)

    else:
        print(response.content)
