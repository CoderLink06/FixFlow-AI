import psycopg2
from langchain_google_vertexai import VertexAIEmbeddings

# --- CONFIGURATION ---
DB_HOST = "35.200.165.186" # Your database IP
DB_NAME = "manuals_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres" # Put your password here!
PROJECT_ID = "zero-downtime-ai"
REGION = "asia-south1"

def main():
    print("1. Initializing Vertex AI...")
    embeddings_model = VertexAIEmbeddings(
        model_name="text-embedding-004", 
        project=PROJECT_ID, 
        location=REGION
    )

    # --- THE SIMULATED EMERGENCY ---
    # Imagine a sensor just sent this text message to our system:
    incoming_alert = "Emergency! Motor B on the conveyor is throwing an ERR-404-TEMP and running super hot. What do we do?"
    
    print(f"\n🚨 INCOMING ALERT: '{incoming_alert}'")
    print("2. Thinking... (Converting alert to vector)")
    
    # Turn the incoming alert into a vector
    alert_vector = embeddings_model.embed_query(incoming_alert)

    print("3. Searching AlloyDB for the exact fix...")
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()

    # This is the magic SQL query. The "<->" operator does a mathematical 
    # similarity search to find the manual whose vector is closest to the alert's vector.
    cur.execute("""
        SELECT error_code, component, resolution
        FROM machine_manuals
        ORDER BY embedding <-> %s::vector
        LIMIT 1;
    """, (str(alert_vector),))

    result = cur.fetchone()

    if result:
        print("\n✅ MATCH FOUND IN KNOWLEDGE BASE:")
        print(f"   Matched Error: {result[0]}")
        print(f"   Target Component: {result[1]}")
        print(f"   Instructions for Tech: {result[2]}\n")
    else:
        print("\n❌ No match found in the database.")

    cur.close()
    conn.close()

if __name__ == "__main__":
    main()