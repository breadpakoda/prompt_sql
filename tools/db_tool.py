from database.db import create_connection
from langchain_core.tools import tool



@tool
def query_executor():
    """
    Executes a query on the mysql database
    """


    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute("show databases")
    print(cursor.description)
    
    