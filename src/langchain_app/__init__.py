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
    
    query = "Write a 200-word essay/paragraph on the use and impact of Artificial Intelligence (AI) in modern society."
    print(f"Invoking model with query: '{query}'\n")
    
    try:
        response = model.invoke(query)
        print("--- Model Output ---")
        print(response.content)
        print("--------------------")
        
        # Word count validation
        words = response.content.split()
        print(f"\nWord count: {len(words)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
