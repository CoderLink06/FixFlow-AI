from langchain_google_vertexai import ChatVertexAI
import traceback

PROJECT_ID = "zero-downtime-ai"
REGION = "us-central1"

print(f"--- Diagnosing Vertex AI in {REGION} for project {PROJECT_ID} ---")
try:
    llm = ChatVertexAI(
        model_name="gemini-1.5-flash", 
        project=PROJECT_ID, 
        location=REGION
    )
    print("Attempting to invoke...")
    llm.invoke("Hi")
    print("Success!")
except Exception as e:
    print("\n!!! ERROR CAUGHT !!!")
    print(f"Exception Type: {type(e)}")
    print(f"Exception Message: {e}")
    print("\nFull Traceback:")
    traceback.print_exc()
