from database.db import create_connection
from langchain_core.tools import tool



@tool
def query_executor(query:str):
    """
    Executes a query on the mysql database
    """
    print("Db executed")

    conn=create_connection()
    cursor=conn.cursor()
    cursor.execute(query)
    if cursor.description:
        return cursor.fetchall()
    else:
        conn.commit()
        return "query executed successuflly"
    cursor.close()
    conn.close()

    
    