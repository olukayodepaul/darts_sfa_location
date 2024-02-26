from connection.posgresql import engine
from sqlalchemy import text

def test_connection():
    try:
        with engine.connect() as conn:
            result = conn.execute(text("SELECT 1"))
            row = result.fetchone()
            if row and row[0] == 1:
                print("Connection to the database established successfully.")
            else:
                print("Connection test failed.")
    except Exception as e:
        print("Error:", e)

