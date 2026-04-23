from .supabase_client import get_supabase

supabase = get_supabase()


def save_message(thread_id: str, query: str, ai_res: str):

    content = {"question": query, "answer": ai_res}
    supabase.table("conversations").insert(
        {
            "thread_id": thread_id,
            "content": content,
        }
    ).execute()


def fetch_messages(thread_id: str):
    response = (
        supabase.table("conversations")
        .select("content")
        .eq("thread_id", thread_id)
        .order("created_at")
        .execute()
    )
    messages = [temp["content"] for temp in response.data]
    return messages
