from langgraph.graph import StateGraph
from app.models.state import AgentState
from app.agents.planner import planner_agent

async def run_workflow(user_input: str):
    state = AgentState(user_input=user_input)

    graph = StateGraph(AgentState)
    graph.add_node("planner", planner_agent)
    graph.set_entry_point("planner")

    app = graph.compile()
    result = app.invoke(state)

    return result.dict()
