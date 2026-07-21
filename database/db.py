import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def create_connection():
    try:
        conn=mysql.connector.connect(
            host=os.getenv("db_host"),
            user=os.getenv("db_user"),
            password=os.getenv("db_password")
        )
        return conn

    except Exception as e:
        raise e
    

