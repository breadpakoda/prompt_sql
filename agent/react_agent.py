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


class SQLReActAgent:
    def __init__(self):
        self.llm=ChatOpenAI(
            base_url=os.getenv("base_url"),
            api_key=os.getenv("api"),
            model=os.getenv("model")
        )

        
        self.tools={
            "query_executor":query_executor,
            "take_user_input" :take_user_input
            }
        
        self.llm=self.llm.bind_tools(
            [
                query_executor,
                take_user_input
            ]
        )

        self.context=[
                    SystemMessage(content="""
                You are a My sql ReAct agent , your task is to generate the mysql queries accrding to the users need and execute it to the DBMS
                """)
                ]

    def invoke(self,user_input):
        self.context.append(HumanMessage(content=user_input))

        while True:
                response=self.llm.invoke(self.context)
                self.context.append(response)

                if response.tool_calls:
                    tool_call=response.tool_calls[0]
                    result=self.tools[response.tool_calls[0]['name']].invoke(tool_call['args'])

                    self.context.append(ToolMessage(content=str(result),
                                                    tool_call_id=tool_call['id'])) 
        
                else:
                    return response.content
                    