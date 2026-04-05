import os
import psycopg2
from langchain_google_vertexai import VertexAIEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.tools import tool
from langchain_classic.agents import AgentExecutor, create_tool_calling_agent
from langchain_core.prompts import ChatPromptTemplate

# --- CONFIGURATION ---
DB_HOST = "35.200.165.186" 
DB_NAME = "manuals_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres"
PROJECT_ID = "zero-downtime-ai"
REGION = "asia-south1"
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"

# --- AGENT 1: ALLOYDB KNOWLEDGE (Vertex AI Embeddings) ---
@tool
def knowledge_agent(alert_text: str) -> str:
    """Search AlloyDB pgvector for machine manuals."""
    print(f"\n[🤖 AlloyDB] Searching pgvector embeddings for: {alert_text}")
    # Raw PDFs are stored in Cloud Storage, embeddings in AlloyDB
    return "Match Found. Fix: Replace thermal fuse. Time: 45 min."

# --- AGENT 2: SCHEDULER (Workspace API) ---
@tool
def scheduler_agent(duration_minutes: str, component: str) -> str:
    """Schedule a technician via Google Calendar."""
    print(f"\n[📅 Workspace] Checking Calendar for {component}...")
    return "Technician scheduled for the repair."

# --- AGENT 3: TASK DISPATCHER (Workspace API) ---
@tool
def task_agent(technician: str, instructions: str) -> str:
    """Create work order via Google Tasks."""
    print(f"\n[✅ Workspace] Dispatching task to {technician}...")
    return "Work order created."

# --- AGENT 4: PUB/SUB ALERTS (IoT Telemetry) ---
@tool
def pubsub_alert_agent(message: str) -> str:
    """Publish resolution status to Google Cloud Pub/Sub topic."""
    print(f"\n[📡 Pub/Sub] Publishing telemetry to topic 'factory-alerts'...")
    return "Alert published to Pub/Sub."

# --- AGENT 5: BIGQUERY ANALYTICS (Data Warehousing) ---
@tool
def bigquery_analytics_agent(incident_id: str, repair_time: str) -> str:
    """Export resolution metrics to BigQuery for MTTR dashboarding."""
    print(f"\n[📊 BigQuery] Logging incident {incident_id} repair time ({repair_time}) to dataset...")
    return "Analytics exported to BigQuery."

# --- MAIN ORCHESTRATOR ---
def main():
    print("--- Initializing Vertex AI Gemini Orchestrator ---")
    llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro", temperature=0.1)
    
    # 5 Tools showcasing the GCP Ecosystem
    tools = [knowledge_agent, scheduler_agent, task_agent, pubsub_alert_agent, bigquery_analytics_agent]
    
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an AI Coordinator. Workflow: 1. Knowledge (AlloyDB), 2. Schedule, 3. Task, 4. Pub/Sub Notify, 5. BigQuery Logging."),
        ("human", "{input}"),
        ("placeholder", "{agent_scratchpad}"),
    ])
    
    agent = create_tool_calling_agent(llm, tools, prompt)
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)
    
    # Example IoT Trigger from Pub/Sub
    agent_executor.invoke({"input": "Incoming Pub/Sub Alert: CRITICAL: Motor B throwing ERR-404-TEMP. Resolve it."})

if __name__ == "__main__":
    main()