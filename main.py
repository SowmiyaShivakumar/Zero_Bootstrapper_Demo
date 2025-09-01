from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username: str
    password: str

@app.post("/login/")
async def login(user: User):
    if user.username == "your_username" and user.password == "your_password":  # Replace with actual validation
        return {"message": "Login successful!"}
    else:
        raise HTTPException(status_code=401, detail="Invalid username or password")

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)