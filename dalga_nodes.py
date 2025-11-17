from dalga_state_scema import AgentState
import json
from langchain_core.messages import SystemMessage, HumanMessage
from dalga_config import INTENT_SYSTEM_PROMPT, SQL_SYSTEM_PROMPT, RESULT_SYSTEM_PROMPT
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
    print(response.content)
    intent = Intent(**intent_json)
    return {'intent':intent}

def clean_sql(sql_response):
    """Remove markdown code blocks and extra whitespace"""
    sql = sql_response.get('sql_query', '')
    # Remove markdown code blocks
    sql = sql.replace('```sql', '').replace('```', '')
    # Strip whitespace
    sql = sql.strip()
    return sql

def sql_generator_node_mock(intent, llm):
    if intent is None:
        raise ValueError("Intent not set")
    
    messages = [
        SystemMessage(content=SQL_SYSTEM_PROMPT),
        HumanMessage(content=intent.model_dump_json())
    ]

    resp = llm.invoke(messages, config={
        "configurable": {
            "response_mime_type": "text/plain"
        }
    })
    sql = clean_sql(resp.content)

    return {"sql_query": sql}


def bigquery_node_mock(sql, bq_client):
    if not sql:
        raise ValueError("SQL query is empty")

    job = bq_client.query(sql)
    rows = [dict(row) for row in job.result()]
    return {"query_result": rows}

def result_interpreter_node_mock(rows, intent, llm):
    message = [
        SystemMessage(content=RESULT_SYSTEM_PROMPT),
        HumanMessage(content=json.dumps({
            "intent": intent.model_dump(),
            "rows": rows 
        }))
    ]

    resp = llm.invoke(message)
    analysis = resp.content
    return {"analysis":analysis}

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