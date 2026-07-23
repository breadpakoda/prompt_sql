from database.db import create_connection
from langchain_core.tools import tool



@tool
def query_executor(query: str):
    """
    Executes one or more MySQL statements.
    """
    conn = create_connection()
    cursor = conn.cursor()

    results = []

    try:
        for result in cursor.execute(query, multi=True):
            if result.with_rows:
                results.append(result.fetchall())

        conn.commit()

        if results:
            return results

        return "Query executed successfully."

    finally:
        cursor.close()
        conn.close()
    

    
    