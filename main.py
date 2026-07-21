# from langchain_openai import ChatOpenAI
# from langchain_core.messages import (
#     SystemMessage,
#     HumanMessage,
#     AIMessage
# )
# import os
# from dotenv import load_dotenv

# load_dotenv()

# llm=ChatOpenAI(
#     base_url=os.getenv("base_url"),
#     api_key=os.getenv("api"),
#     model=os.getenv("model")
# )

# context=[
#     SystemMessage(content="Respond to the user query")
# ]

# user_input=input("Query: ")
# context.append(HumanMessage(content=user_input))

# response=llm.invoke(context)
# print(response.content)


from tools.db_tool import query_executor

query_executor()