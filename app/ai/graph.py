from typing import Annotated
from typing_extensions import TypedDict

from langchain_core.messages import BaseMessage
from langchain_core.messages import SystemMessage
from langgraph.graph.message import add_messages

from langchain_google_genai import ChatGoogleGenerativeAI
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import ToolNode

from app.core.config import settings

from app.ai.tools import (
    count_students,
    find_student,
    get_students_by_department
)


# -----------------------------------
# 1. Define chatbot state
# -----------------------------------

class AgentState(TypedDict):

    messages: Annotated[
        list[BaseMessage],
        add_messages
    ]


# -----------------------------------
# 2. Define tools
# -----------------------------------

tools = [
    count_students,
    find_student,
    get_students_by_department,
    
]

# -----------------------------------
# 3. Create Gemini model
# -----------------------------------

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=0,
    google_api_key=settings.gemini_api_key
)


# Give Gemini access to our tools

model = llm.bind_tools(tools)


# -----------------------------------
# 4. Gemini node
# -----------------------------------

def call_model(state: AgentState):

    system_message = SystemMessage(
        content="""
You are a Student Database Assistant.

You help users retrieve information
from the student database.

Rules:

1. Use database tools when the user
   asks about student information.

2. Do not invent student information.

3. If the database does not contain
   the requested information, say so.

4. Give simple and clear answers.

5. Do not expose database passwords,
   API keys, or internal system details.
"""
    )

    messages = [
        system_message
    ] + state["messages"]

    response = model.invoke(messages)

    return {
        "messages": [response]
    }


# -----------------------------------
# 5. Tool node
# -----------------------------------

tool_node = ToolNode(tools)


# -----------------------------------
# 6. Decide what happens next
# -----------------------------------

def should_continue(state: AgentState):

    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "end"


# -----------------------------------
# 7. Create graph
# -----------------------------------

workflow = StateGraph(AgentState)


workflow.add_node(
    "chatbot",
    call_model
)


workflow.add_node(
    "tools",
    tool_node
)


workflow.set_entry_point(
    "chatbot"
)


workflow.add_conditional_edges(
    "chatbot",
    should_continue,
    {
        "tools": "tools",
        "end": END
    }
)


workflow.add_edge(
    "tools",
    "chatbot"
)


# -----------------------------------
# 8. Compile graph
# -----------------------------------

graph = workflow.compile()