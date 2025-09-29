from flask import Flask, render_template
import mysql.connector
import os

app = Flask(__name__)

DB_HOST = os.environ.get("DB_Host", "mysql")
DB_USER = os.environ.get("DB_User", "root")
DB_PASS = os.environ.get("DB_Password", "db_pass123")
DB_NAME = os.environ.get("DB_Name", "mydb")

@app.route("/")
def index():
    try:
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASS,
            database=DB_NAME
        )
        cursor = conn.cursor()
        cursor.execute("SELECT 'Hello from MySQL!'")
        result = cursor.fetchone()
        cursor.close()
        conn.close()
        return f"<h1>Flask is running!</h1><p>{result[0]}</p>"
    except Exception as e:
        return f"<h1>Flask is running!</h1><p>Error: {str(e)}</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)