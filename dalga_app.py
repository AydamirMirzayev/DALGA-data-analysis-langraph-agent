from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import bigquery
from dalga_graph import create_graph
from conversation_memory import ConversationMemory
import os

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
        
        return ""