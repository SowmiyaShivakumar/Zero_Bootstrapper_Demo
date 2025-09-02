from fastapi import FastAPI
from ecommerce_app.routes import router as ecommerce_router

app = FastAPI()

# Include ecommerce routes
app.include_router(ecommerce_router)

@app.get("/")
async def read_root():
    return {"message": "Hello, FastAPI!"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)