from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/login", response_class=HTMLResponse)
async def login_form():
    return '''<form action="/login" method="post">
                <input type="text" name="username" placeholder="Username">
                <input type="password" name="password" placeholder="Password">
                <input type="submit" value="Login">
              </form>'''  

@app.post("/login")
async def login(username: str = Form(...), password: str = Form(...)):
    # Simple hardcoded username and password for demonstration
    if username == "admin" and password == "secret":
        return {"message": "Login successful"}
    else:
        return {"message": "Invalid credentials"}

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)