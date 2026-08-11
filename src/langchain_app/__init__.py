import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def main() -> None:
    # Load environment variables from .env file
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY is not set.")
        return
        
    print("Initializing ChatGoogleGenerativeAI model (gemini-2.5-flash)...")
    try:
        # Initialize Gemini 2.5 Flash model (since 1.5-flash is not available in the API list for this key)
        model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
        
        print("Invoking model with test query...")
        response = model.invoke("Write a short 1-sentence welcome message for someone starting an Agentic AI course.")
        print("\nResponse:")
        print(response.content)
    except Exception as e:
        print(f"\nError running Gemini query: {e}")

if __name__ == "__main__":
    main()
