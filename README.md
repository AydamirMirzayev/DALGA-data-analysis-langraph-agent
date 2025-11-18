# Data Analysis LangGraph Agent: DALGA
 Data analysis Agent for ```bigquery-public-data.thelook_ecommerce``` dataset

Backbone LLM used during development: ```gemini-2.0-flash```

## Refer to:

High-level architecture in:[```architecture.md```](architecture.md)

Sample run in: [```sample-run.md```](sample-run.md)


## Setup Instructions:
### 1. Copy the repository

### 2. Install Dependencies 
```bash
pip install requirements.txt
```
### 3. Create .env for Google Cloud and Google AI Studios credentials
```python
GOOGLE_API_KEY="your-google-api-key"
GOOGLE_CLOUD_PROJECT_ID="google-cloud-project-id"
```
### 4. Run ```main.py``` for demo

Tested with Python 3.10.11
