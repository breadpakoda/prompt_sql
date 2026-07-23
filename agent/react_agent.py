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
from langgraph.graph import StateGraph, START, END
from agent.state import AgentState

load_dotenv()


class SQLReActAgent:
    def __init__(self):
        self.llm=ChatOpenAI(
            base_url=os.getenv("base_url"),
            api_key=os.getenv("api"),
            model=os.getenv("model")
        )

        
        self.tool_map={
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

        self.graph=self.build_graph()

   
    def graph_invoke(self, user_input):

        state = {
        "messages": self.context + [HumanMessage(content=user_input)]
        }

        result = self.graph.invoke(state)

        self.context = result["messages"]

        return self.context[-1].content
    


    def build_graph(self):
        builder=StateGraph(AgentState)
        builder.add_node("chatbot", self.chatbot)
        builder.add_node("tools", self.tools)
        builder.add_edge(START, "chatbot")
        builder.add_conditional_edges(
        "chatbot",
        self.should_continue
        )
        builder.add_edge("tools", "chatbot")

        return builder.compile()
    

    def chatbot(self, state: AgentState):

        response = self.llm.invoke(state["messages"])

        return {
        "messages": state["messages"] + [response]
        }

    def should_continue(self, state: AgentState):

        last_message = state["messages"][-1]

        if last_message.tool_calls:
            return "tools"

        return END


    def tools(self, state: AgentState):

        last_message = state["messages"][-1]

        tool_messages = []

        for tool_call in last_message.tool_calls:

            result = self.tool_map[tool_call["name"]].invoke(tool_call["args"])

            tool_messages.append(
                ToolMessage(
                    content=str(result),
                    tool_call_id=tool_call["id"]
                )
            )

        return {
            "messages": state["messages"] + tool_messages
        }