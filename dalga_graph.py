from dalga_nodes import intent_parser_node, sql_generator_node, bigquery_node
from dalga_nodes import result_interpreter_node, answer_node
from dalga_state_scema import AgentState
from langgraph.graph import StateGraph, END


def create_graph():
    graph = StateGraph(AgentState)

    graph.add_node("parse_intent", intent_parser_node)
    graph.add_node("generate_sql", sql_generator_node)
    graph.add_node("run_bigquery", bigquery_node)
    graph.add_node("interpret_results", result_interpreter_node)
    graph.add_node("form_answer", answer_node)


    graph.set_entry_point("parse_intent")
    graph.add_edge("parse_intent", "generate_sql")
    graph.add_edge("generate_sql", "run_bigquery")
    graph.add_edge("run_bigquery", "interpret_results")
    graph.add_edge("interpret_results", "form_answer")
    graph.add_edge("form_answer", END)

    return graph.compile()
