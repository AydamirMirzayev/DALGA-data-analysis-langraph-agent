from langchain_google_genai import ChatGoogleGenerativeAI
from google.cloud import bigquery
import os

class DalgaApp:
    "Application class to manage graph lifecycle"

    def __init__(self):
        self.llm  = ChatGoogleGenerativeAI(
                    model="gemini-2.0-flash",
                    api_key=os.environ["GOOGLE_API_KEY"]
        )

        self.bq_client = bigquery.Client(project=os.environ["GOOGLE_COUD_PROJECT_ID"])

        

