from app.core.llm import get_llm

llm = get_llm()

def planner_agent(state):
    prompt = f'''
    Break this project into clear steps:
    {state.user_input}
    '''
    response = llm.predict(prompt)
    state.plan = response.split("\n")
    return state
