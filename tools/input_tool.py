from langchain_core.tools import tool

@tool
def take_user_input(description:str):
    """
    Tool to take the user input in case of information requirment.
    """
    return input(description)