from agent.react_agent import SQLReActAgent

agent= SQLReActAgent()

while True:
    user_input=input("Query: ")
    answer=agent.invoke(user_input)
    print(answer)

   



    
