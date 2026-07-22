from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
    ToolMessage
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
tools={"query_executor":query_executor,
       "take_user_input" :take_user_input}
tool_binded_llm=llm.bind_tools(
    [
        query_executor,
        take_user_input
    ]
)
while True:
    user_input=input("Query: ")
    context.append(HumanMessage(content=user_input))

   



    while True:
        response=tool_binded_llm.invoke(context)
        context.append(response)
    
        if response.tool_calls:
            
            context.append(ToolMessage(content=tools[response.tool_calls[0]['name']].invoke(response.tool_calls[0]['args']),
                                       tool_call_id=response.tool_calls[0]['id'])) 

        else:
            print(response.content)
            break
# [{'name': 'query_executor', 'args': {'query': 'SHOW DATABASES;'}, 'id': 'call-f9cff72f-50c4-4934-b815-4e7c05e42af6', 'type': 'tool_call'}]