import os
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
import pymysql

app = Flask(__name__)

# Security Hardening: Load credentials from environment variables instead of hardcoding
DB_USER = os.getenv("DB_USER", "root")
DB_PASSWORD = os.getenv("DB_PASSWORD", "")
DB_NAME = os.getenv("DB_NAME", "testdb")
DB_HOST = os.getenv("DB_HOST", "localhost")

app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

def createQuery():
    # Secure Parameterized Query Template
    return "SELECT * FROM users WHERE username = %s AND password = %s"

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get('username', '')
        password = request.form.get('password', '')

        connection = pymysql.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD,
            database=DB_NAME
        )
        cursor = connection.cursor()

        # Fix: Query string and parameters passed separately to the driver
        query = createQuery()
        cursor.execute(query, (username, password))
        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result:
            return "Login successful!"
        else:
            return "Invalid credentials."

    return '''
        <form method="post">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit" value="Login">
        </form>
    '''

if __name__ == "__main__":
    # Security Hardening: Disable interactive debug mode
    app.run(debug=False)
