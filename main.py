from fastapi import FastAPI
import os
import sqlite3
import random

app = FastAPI(debug=True)  # ❌ Security issue: debug mode enabled

# ❌ Hardcoded secret
API_SECRET = "1234567890SUPERSECRET"


@app.get("/")
def read_root():
    unused_variable = "this variable is never used"  # ❌ code smell

    return {"message": "Hello World from FastAPI!", "status": "online"}


@app.get("/health")
def health_check():
    return {"status": "healthy"}


# ❌ SQL Injection vulnerability
@app.get("/user")
def get_user(username: str):
    conn = sqlite3.connect("users.db")
    cursor = conn.cursor()

    # vulnerable query
    query = f"SELECT * FROM users WHERE username = '{username}'"
    cursor.execute(query)

    result = cursor.fetchall()
    return {"data": result}


# ❌ Command Injection
@app.get("/ping")
def ping(host: str):
    return os.system("ping -c 1 " + host)


# ❌ Dangerous eval
@app.get("/calculate")
def calculate(expr: str):
    return {"result": eval(expr)}


# ❌ Weak random
@app.get("/token")
def generate_token():
    return {"token": random.random()}


if __name__ == "__main__":
    import uvicorn

    port = int(os.environ.get("PORT", 8080))
    uvicorn.run(app, host="0.0.0.0", port=port)