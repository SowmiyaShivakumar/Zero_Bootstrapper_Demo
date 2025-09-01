from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BMIInput(BaseModel):
    weight: float
    height: float

@app.post('/calculate_bmi')
async def calculate_bmi(input: BMIInput):
    bmi = input.weight / (input.height ** 2)
    return {'bmi': bmi}

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)