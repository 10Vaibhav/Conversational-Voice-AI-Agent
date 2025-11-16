import asyncio
from speech_handler import SpeechHandler
from memory_manager import MemoryManager
from ai_agent import AIAgent

class VoiceAgent:
    """Main voice assistant orchestrator."""
    
    def __init__(self, user_id: str = "Mahajan"):
        self.user_id = user_id
        self.speech_handler = SpeechHandler()
        self.memory_manager = MemoryManager(user_id)
        self.ai_agent = AIAgent()
    
    async def process_conversation(self):
        """Process a single conversation turn."""
        # Listen to user
        user_input = self.speech_handler.listen()
        
        # Search for relevant memories
        print("Searching memories...")
        memories = self.memory_manager.search(user_input)
        print("Found Memories:", memories)
        
        # Generate AI response
        ai_response = self.ai_agent.get_response(user_input, memories)
        print("AI Response:", ai_response)
        
        # Speak the response
        await self.speech_handler.speak(ai_response)
        
        # Save to memory
        print("Saving to memory...")
        self.memory_manager.add(user_input, ai_response)
        print("Memory saved.")
    
    def run(self):
        """Run the voice assistant in a loop."""
        print("Voice Assistant started. Listening...")
        
        while True:
            try:
                asyncio.run(self.process_conversation())
            except KeyboardInterrupt:
                print("\nVoice Assistant stopped.")
                break
            except Exception as e:
                print(f"Error: {e}")
                continue

def main():
    assistant = VoiceAgent(user_id="Mahajan")
    assistant.run()

if __name__ == "__main__":
    main()


