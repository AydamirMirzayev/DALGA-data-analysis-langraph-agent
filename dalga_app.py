from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import bigquery
from dalga_graph import create_graph
from conversation_memory import ConversationMemory
from dalga_state_scema import AgentState
import os
from dotenv import load_dotenv
load_dotenv()

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

    
    def forward(self, user_question: str) -> str:
        """ Single forward pass of graph execution initiated by user question"""
        initial_state = AgentState(
            parser_input=user_question,
            memory_context=self.memory.get_memory()
        )

        config = {
                    "configurable": {
                        "llm": self.llm,
                        "bq_client": self.bq_client
                    }
        }

        final_state = self.graph.invoke(initial_state, config=config)

        answer = final_state.get("final_answer", "No answer generated")
                

        self.memory.add_interaction(
                    user_input=user_question,
                    final_answer=answer
        )

        return answer