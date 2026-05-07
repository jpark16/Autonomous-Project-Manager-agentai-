from fastapi import APIRouter
from app.graph.workflow import run_workflow

router = APIRouter()

@router.post("/generate")
async def generate_project(prompt: str):
    result = await run_workflow(prompt)
    return {"result": result}
