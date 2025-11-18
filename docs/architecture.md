# Data Analysis LangGraph Agent: DALGA
## Atchitecuture

### ```DalgaApp```: 

Is the final wrapper class that stores ```LangGraph```, ```ChatGoogleGenerativeAI```, ```google.cloud.bigquery```, and ```ConversationMemory``` instances for a single session

```Python
class DalgaApp:
    "Application class to manage graph lifecycle"
    def __init__(self):
        # Gemini instance
        self.llm  = ChatGoogleGenerativeAI(
                    model="gemini-2.0-flash",
                    api_key=os.environ["GOOGLE_API_KEY"]
        )
        
        # GC client instance
        self.bq_client = bigquery.Client(project=os.environ["GOOGLE_COUD_PROJECT_ID"])
        # LangGrap instance
        self.graph = create_graph()
        # Memory instance 
        self.memory = ConversationMemory()
```

#### Components:

* ```LangGraph```: Connects the nodes, passes a single instance of **llm** and **BigQuery** client to the nodes
* ```ChatGoogleGenerativeAI``` tested with **gemini-2.0-flash**
* ```google.cloud.bigquery``` BigQuery client
* ```ConversationMemory``` stores conversation memory from the latest interaction

#### Execution:

Graph is executed using ```forward()``` function. During execution an instance of ```AgentState``` is created and preserved for a single pass (question), and does not persist for the entire session. Conversation memory is preserved using an instance of ```ConversationMemory```

### ```ConversationMemory:```

Is a Python class used to preserve the conversation memory throughrout the session. Can be cleared mid-session using ```clear()``` . In the current implementation stores only latest question and response, to account for a follow up question. Can be modified to incorporate more conversation data such as node outputs, or multi depth conversation history.


### ```AgentState:``` 
Inherits **BaseModel** from  **Pydantic**. Defines the state strcure for the graph defined in ```dalga_state_scema.py```

```Python
class AgentState(BaseModel):
    parser_input: str
    memory_context: Dict[str, Any]
    intent: Optional[Intent] = None
    sql_query: Optional[str] = None
    query_result: Optional[List[Dict[str, Any]]] = None
    analysis: Optional[str] = None
    final_answer: Optional[str] = None
```

#### Special components:

Parsed intent defined to parse unstructure user question to a structure intent for the sql generator node

```Python 
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
````

### ```DAG Graph Implementation:```

Direct Acyclic Graph implementation using ```LangGraph```. Graph is executed directionally in the order provided below. Thus the edges form between consecutive nodes, with the answer node being the final one. 

### Nodes defined in ```dalga_nodes.py```:


* ```intent_parser_node:``` Converts unstructured input text text into structured intent for SQL genrator function using gemini model

* ```sql_generator_node:``` Generates the SQL query using gemini model.

* ```bigquery_node:``` Tool calling, executes BigQuery 

* ```result_interpreter_node:``` Interpret the rows of the query result. Provide general answer.

* ```answer_node:``` Placeholder for output tone/brevity/style adjustment as necessary.


## ```config.py:```
Stores prompt templates for the agent

Components:

* INTENT_SYSTEM_PROMPT

* SQL_SYSTEM_PROMPT

* RESULT_SYSTEM_PROMPT

## ```main.py```

#### CLI implmentation
    
    Question: 'you question'

    'quit' to teminate, and 'clear' to clear conversation memory.