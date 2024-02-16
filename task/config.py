from dotenv import load_dotenv
import os

load_dotenv()

config = {
    'api_key': os.getenv("API_KEY"),
    'auth_domain': os.getenv("AUTH_DOMAIN"),
    'project_id': os.getenv("PROJECT_ID"),
    'storage_bucket': os.getenv("STORAGE_BUCKET"),
    'messaging_sender_id': os.getenv("MESSAGING_SENDER_ID"),
    'app_id': os.getenv("APP_ID"),
}
