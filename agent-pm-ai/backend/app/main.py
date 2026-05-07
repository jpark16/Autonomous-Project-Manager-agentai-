from fastapi import FastAPI
from app.api.routes import router

app = FastAPI(title="Agent PM AI")

app.include_router(router)

@app.get("/")
def root():
    return {"message": "Agent PM AI running"}
