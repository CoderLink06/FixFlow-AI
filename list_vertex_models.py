from google.cloud import aiplatform

PROJECT_ID = "zero-downtime-ai"
REGION = "us-central1"

def list_models():
    aiplatform.init(project=PROJECT_ID, location=REGION)
    model_list = aiplatform.Model.list()
    for model in model_list:
        print(f"Model: {model.display_name}, ID: {model.name}")

if __name__ == "__main__":
    try:
        list_models()
    except Exception as e:
        print(f"Error listing models: {e}")
