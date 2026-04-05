import psycopg2
from langchain_google_vertexai import VertexAIEmbeddings

# --- CONFIGURATION ---
DB_HOST = "35.200.165.186" # From your previous screenshot
DB_NAME = "manuals_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres" # Put your password here!
PROJECT_ID = "zero-downtime-ai"
REGION = "asia-south1"

# --- THE MACHINE MANUAL DATA ---
# This is the "fake" manual data we are feeding the AI for the demo
manuals = [
    {
        "error_code": "ERR-404-TEMP",
        "component": "Conveyor_Motor_B",
        "description": "Overheating detected in the primary conveyor motor.",
        "resolution": "Blown thermal fuse identified. Immediate replacement required. Estimated repair time: 45 minutes. Tools needed: 10mm wrench, replacement fuse part #F-99."
    },
    {
        "error_code": "ERR-802-PRES",
        "component": "Hydraulic_Pump_A",
        "description": "Low pressure detected in the main hydraulic line.",
        "resolution": "Check for fluid leaks at the primary valve. If no leak, replace the main seal. Estimated repair time: 60 minutes. Tools needed: Seal kit #S-22, fluid catch pan."
    },
    {
        "error_code": "ERR-101-MECH",
        "component": "Packaging_Arm",
        "description": "Misalignment in the robotic packaging arm.",
        "resolution": "Recalibrate the X-axis servo. Do not replace parts unless physical damage is visible. Estimated repair time: 15 minutes. Tools needed: Diagnostics tablet, calibration laser."
    }
]

def main():
    print("1. Initializing Vertex AI Embeddings...")
    # This connects to Google's AI to turn our text into meaning-based vectors
    embeddings_model = VertexAIEmbeddings(
        model_name="text-embedding-004", 
        project=PROJECT_ID, 
        location=REGION
    )

    print("2. Connecting to AlloyDB...")
    conn = psycopg2.connect(host=DB_HOST, dbname=DB_NAME, user=DB_USER, password=DB_PASSWORD)
    cur = conn.cursor()

    print("3. Creating the vector database table...")
    # text-embedding-004 creates vectors with 768 dimensions
    cur.execute("""
        CREATE TABLE IF NOT EXISTS machine_manuals (
            id SERIAL PRIMARY KEY,
            error_code VARCHAR(50),
            component VARCHAR(50),
            description TEXT,
            resolution TEXT,
            embedding vector(768) 
        );
    """)
    cur.execute("TRUNCATE TABLE machine_manuals;") # Clears out old data if you run this twice
    
    print("4. Processing manuals and saving to database...")
    for manual in manuals:
        # We want the AI to understand the WHOLE situation, so we combine the text before embedding it
        text_to_embed = f"Error: {manual['error_code']} on {manual['component']}. Symptoms: {manual['description']}. Fix: {manual['resolution']}"
        
        # Turn the text into a vector using Vertex AI
        vector = embeddings_model.embed_query(text_to_embed)
        
        # Save everything to AlloyDB
        cur.execute(
            "INSERT INTO machine_manuals (error_code, component, description, resolution, embedding) VALUES (%s, %s, %s, %s, %s)",
            (manual["error_code"], manual["component"], manual["description"], manual["resolution"], vector)
        )
        print(f"   -> Inserted {manual['error_code']} into database.")

    conn.commit()
    cur.close()
    conn.close()
    print("\n✅ SUCCESS! The AI Knowledge Base is fully loaded.")

if __name__ == "__main__":
    main()