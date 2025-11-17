from typing import List, Optional, Dict, Any
from pydantic import BaseModel

class Filter(BaseModel):
    column: str
    operator: str
    value: Any

class Ordering(BaseModel):
    by: str
    direction: str  # "asc" or "desc"

class Intent(BaseModel):
    operation: str
    metrics: List[str]
    entities: List[str]
    filter: List[Filter] = []
    time_range: Optional[str] = None
    granuality: Optional[str] = None 
    group_by: List[str] = []
    ordering: Optional[Ordering] = None 
    limit: Optional[int] = None
    notes: Optional[str] = None

class AgentState(BaseModel):
    parser_imput: str
    memory_context: Dict[str, Any]
    intent: Optional[Intent] = None
    sql_query: Optional[str] = None
    query_result: Optional[List[Dict[str, Any]]] = None
    analysis: Optional[str] = None
    final_answer: Optional[str] = None
