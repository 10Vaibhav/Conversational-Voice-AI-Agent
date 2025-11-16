import speech_recognition as sr
from openai import AsyncOpenAI
from openai.helpers import LocalAudioPlayer

class SpeechHandler:
    """Handles speech-to-text and text-to-speech operations."""
    
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.async_client = AsyncOpenAI()
    
    def listen(self) -> str:
        """Listen to microphone and convert speech to text."""
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            self.recognizer.pause_threshold = 2
            
            print("Speak something...")
            audio = self.recognizer.listen(source)
            
            print("Processing Audio... (STT)")
            text = self.recognizer.recognize_google(audio)
            print("You Said:", text)
            
            return text
    
    async def speak(self, text: str):
        """Convert text to speech and play it."""
        async with self.async_client.audio.speech.with_streaming_response.create(
            model="gpt-4o-mini-tts",
            voice="coral",
            instructions="Always speak in cheerful manner with full of delight and happy",
            input=text,
            response_format="pcm"
        ) as response:
            await LocalAudioPlayer().play(response)