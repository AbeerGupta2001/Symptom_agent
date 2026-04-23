from supabase import Client, create_client
from dotenv import load_dotenv
import os
from functools import lru_cache

load_dotenv()

SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_SECRET_KEY")


@lru_cache()
def get_supabase() -> Client:
    return create_client(supabase_url=SUPABASE_URL, supabase_key=SUPABASE_KEY)
