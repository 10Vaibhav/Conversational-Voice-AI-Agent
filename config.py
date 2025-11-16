import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    """Configuration management for the voice assistant."""
    
    OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
    NEO_CONNECTION_URL = os.getenv("NEO_CONNECTION_URL")
    NEO_USERNAME = os.getenv("NEO_USERNAME")
    NEO_PASSWORD = os.getenv("NEO_PASSWORD")
    
    @staticmethod
    def get_memory_config():
        """Returns the memory configuration for mem0."""
        return {
            "version": "v1.1",
            "embedder": {
                "provider": "openai",
                "config": {
                    "api_key": Config.OPENAI_API_KEY,
                    "model": "text-embedding-3-small"
                }
            },
            "llm": {
                "provider": "openai",
                "config": {
                    "api_key": Config.OPENAI_API_KEY,
                    "model": "gpt-4.1"
                }
            },
            "graph_store": {
                "provider": "neo4j",
                "config": {
                    "url": Config.NEO_CONNECTION_URL,
                    "username": Config.NEO_USERNAME,
                    "password": Config.NEO_PASSWORD
                }
            },
            "vector_store": {
                "provider": "qdrant",
                "config": {
                    "host": "localhost",
                    "port": 6333
                }
            }
        }
