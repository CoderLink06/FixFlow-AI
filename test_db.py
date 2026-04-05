import psycopg2

# --- CONFIGURATION ---
DB_HOST = "35.200.165.186"
DB_NAME = "manuals_db"
DB_USER = "postgres"
DB_PASSWORD = "postgres" # The one you wrote down earlier!

try:
    # 1. Attempt to connect to the database
    print("Attempting to connect to AlloyDB...")
    conn = psycopg2.connect(
        host=DB_HOST,
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port="5432"
    )
    
    # 2. Run a simple test query
    cur = conn.cursor()
    cur.execute("SELECT version();")
    db_version = cur.fetchone()
    
    print("\n✅ SUCCESS! Connected to the database.")
    print(f"Database Info: {db_version[0]}\n")
    
    # 3. Enable the AI extensions we need for the next step
    cur.execute("CREATE EXTENSION IF NOT EXISTS vector;")
    cur.execute("CREATE EXTENSION IF NOT EXISTS google_ml_integration;")
    conn.commit()
    print("✅ AI Vector extensions enabled successfully!")

    cur.close()
    conn.close()

except Exception as e:
    print("\n❌ CONNECTION FAILED:")
    print(e)