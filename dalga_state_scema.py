from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class AgentState(BaseModel):
    parser_imput: str
    memory_context: Dict[str, Any]
    intent: Dict[str, any]
    sql_query: Dict[str, any]
    query_result: any
    resonse: str

