from typing import TypedDict
from langgraph.graph import END, StateGraph


# State
class State(TypedDict):
    number: int


# Nodes
def double(state: State) -> dict:
    boardNum = state["number"]
    newNum = boardNum * 2
    print("In double:", newNum)
    
    return {"number": newNum}

def finish(state: State) -> dict:
    boardNum = state["number"]
    print("In finish:", boardNum)
    
    return {"number": boardNum}

def decision(state: State) -> str:
    if state["number"] < 100:
        return "double"
    else:
        return "finish"
    

# Initialize the Graph
builder = StateGraph(State)

# Adding Nodes to the Graph
builder.add_node("double", double)
builder.add_node("finish", finish)

# Entry Point
builder.set_entry_point("double")

builder.add_conditional_edges(
    "double",
    decision,
    {"double": "double", "finish": "finish"}
)

builder.add_edge("finish", END)


# Making the Graph
graph = builder.compile()


if __name__ == "__main__":
    result = graph.invoke({"number": 5, "log": ""})
