from mem0 import Memory
from config import Config

class MemoryManager:
    """Handles memory operations using mem0."""
    
    def __init__(self, user_id: str):
        self.user_id = user_id
        self.client = Memory.from_config(Config.get_memory_config())
    
    def search(self, query: str) -> list:
        """Search for relevant memories based on query."""
        search_results = self.client.search(query=query, user_id=self.user_id)
        memories = [
            f"ID: {mem.get('id')}\nMemory: {mem.get('memory')}"
            for mem in search_results.get("results", [])
        ]
        return memories
    
    def add(self, user_message: str, assistant_message: str):
        """Add a conversation to memory."""
        self.client.add(
            user_id=self.user_id,
            messages=[
                {"role": "user", "content": user_message},
                {"role": "assistant", "content": assistant_message}
            ]
        )
