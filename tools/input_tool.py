from langchain_core.tools import tool

@tool
def take_user_input(description:str):
    """
    Tool to take the user input in case of information requirment.
    """

    print("Enter the input")
    return input(description)