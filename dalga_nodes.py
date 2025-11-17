from dalga_state_scema import AgentState
import json
from langchain_core.messages import SystemMessage, HumanMessage
from dalga_config import INTENT_SYSTEM_PROMPT
from dalga_state_scema import Intent

def intent_parser_node_mock(memory_context, user_input, llm):
    messages = [
        SystemMessage(content=INTENT_SYSTEM_PROMPT),
        HumanMessage(content=json.dumps({
            "user_input" : user_input,
            "memory_context" : memory_context
        }))
    ]

    response = llm.invoke(messages, generation_config={
        "response_mime_type": "application/json"
    })
    intent_json = json.loads(response.content)
    intent = Intent(**intent_json)
    return {'intent':intent}

def intent_parser_node(state: AgentState) -> dict:
    return ""

def  sql_generator_node(state: AgentState) -> dict:
    return ""

def bigquery_node(state: AgentState) -> dict:
    return ""

def result_interpreter_node(state: AgentState) -> dict:
    return ""

def answer_node(state: AgentState) -> dict:
    return ""