"""
Simple test to check if Gemini API works
"""
import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Get API key
api_key = os.getenv('GEMINI_API_KEY')
print(f"1. API Key found: {api_key[:20]}...")

# Try to configure Gemini
try:
    genai.configure(api_key=api_key)
    print("2. Gemini configured successfully")

    # List available models
    print("\n3. Available models:")
    for model in genai.list_models():
        if 'generateContent' in model.supported_generation_methods:
            print(f"   - {model.name}")

    # Try to use a model
    print("\n4. Testing with gemini-pro model...")
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content("Say 'Hello World' in one word")
    print(f"   Response: {response.text}")
    print("\n✅ SUCCESS! Your Gemini API is working!")

except Exception as e:
    print(f"\n❌ ERROR: {e}")
    print("\nYour API key may be invalid or expired.")
    print("Follow the instructions below to get a new one.")
