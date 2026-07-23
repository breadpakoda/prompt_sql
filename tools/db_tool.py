from database.db import create_connection
from langchain_core.tools import tool
import sqlparse


@tool
def query_executor(query: str):
    """
    Executes one or more SQL statements on a MySQL database.
    """

    print("Db executed")
    print("=" * 80)
    print(query)
    print("=" * 80)

    conn = create_connection()
    cursor = conn.cursor()

    statements = sqlparse.split(query)

    results = []

    try:
        for stmt in statements:

            stmt = stmt.strip()

            if not stmt:
                continue

            try:
                cursor.execute(stmt)

                if cursor.description:
                    data = cursor.fetchall()

                    results.append({
                        "statement": stmt,
                        "status": "success",
                        "rows": data
                    })

                else:
                    results.append({
                        "statement": stmt,
                        "status": "success",
                        "message": "Executed successfully"
                    })

            except Exception as e:

                conn.rollback()

                return {
                    "status": "failed",
                    "statement": stmt,
                    "error": str(e)
                }

        conn.commit()

        return {
            "status": "success",
            "results": results
        }

    finally:
        cursor.close()
        conn.close()