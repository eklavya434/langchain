import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

def main() -> None:
    # Load environment variables
    load_dotenv()
    
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        print("Error: GOOGLE_API_KEY is not set.")
        return
        
    print("Initializing Gemini model (gemini-2.5-flash)...")
    model = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
    
    query = "Write me a 200 words paragraph on Artificial Intelligence"
    print(f"Streaming response for query: '{query}'\n")
    
    try:
        # Using model.stream() to print response progressively in real-time
        for chunk in model.stream(query):
            print(chunk.content, end="", flush=True)
        print("\n\n--- Streaming Completed ---")
    except Exception as e:
        print(f"\nError: {e}")

if __name__ == "__main__":
    main()
