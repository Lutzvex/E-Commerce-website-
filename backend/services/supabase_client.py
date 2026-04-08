from supabase import create_client, Client
from config import Config

def init_supabase() -> Client:
    url: str = Config.SUPABASE_URL
    key: str = Config.SUPABASE_KEY
    if not url or not key:
        print("Warning: SUPABASE_URL or SUPABASE_KEY is missing")
        return None
    return create_client(url, key)

supabase: Client = init_supabase()
