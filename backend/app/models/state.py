from pydantic import BaseModel
from typing import List, Dict, Any

class AgentState(BaseModel):
    user_input: str
    plan: List[str] = []
    architecture: str = ""
    code: str = ""
    tests: str = ""
    tickets: List[Dict[str, Any]] = []
