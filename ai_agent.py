import json
from openai import OpenAI

class AIAgent:
    """Handles AI conversation logic."""
    
    def __init__(self):
        self.client = OpenAI()
    
    def get_response(self, user_input: str, memories: list) -> str:
        """Generate AI response based on user input and memories."""
        system_prompt = f"""
        You're an expert voice agent. You are given the transcript of what user has said using voice.
        You need to output as if you are an voice agent and whatever you speak will be converted back
        to audio using AI and played back to user.

        Here is the context about the user:
        {json.dumps(memories)}
        """
        
        response = self.client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_input}
            ]
        )
        
        return response.choices[0].message.content
