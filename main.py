"""Application entry point — wires all modules together."""

from config.settings import DEBUG, DATABASE_URL
from backend.database import get_user, get_orders_by_user
from services.auth_service import AuthenticationService
from services.ai_assistant import AIAssistant
from api.files import UPLOAD_DIR, download_file
from utils.file_processor import process_file, resize_image
from cache.session_cache import SessionCache
from utils.ai_helpers import detect_objects, embed_text
from security.hashing import hash_password, sign_token

def create_app():
    auth = AuthenticationService(DATABASE_URL)
    cache = SessionCache()
    ai = AIAssistant()
    return auth, cache, ai

if __name__ == "__main__":
    app_auth, app_cache, app_ai = create_app()
    print(f"Running in debug={DEBUG}")
