import os
from dotenv import load_dotenv
from langchain_core.tools import tool
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, ToolMessage

# 1. Define the custom weather tool using the @tool decorator.
@tool
def get_weather(location: str) -> str:
    """Get the current weather for a given location."""
    location_lower = location.lower()
    if "tokyo" in location_lower:
        return "The weather in Tokyo is rainy and 18°C."
    elif "new york" in location_lower:
        return "The weather in New York is sunny and 27°C."
    elif "london" in location_lower:
        return "The weather in London is cloudy and 15°C."
    else:
        return f"The weather in {location} is pleasant and 22°C."

def main() -> None:
    # Load environment variables from .env file
    load_dotenv()
    
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        print("Error: OPENAI_API_KEY is not set in your .env file.")
        print("Please add your OpenAI API key to the .env file like this:")
        print("OPENAI_API_KEY=your-openai-api-key")
        return
        
    print("1. Initializing ChatOpenAI model (gpt-4o-mini)...")
    model = ChatOpenAI(model="gpt-4o-mini")
    
    # 2. Bind the tool to the model.
    print("2. Binding the 'get_weather' tool to the OpenAI model...")
    model_with_tools = model.bind_tools([get_weather])
    
    # 3. Ask a question that requires the tool.
    query = "What is the weather like in Tokyo right now?"
    print(f"\n3. Sending query to model: '{query}'")
    
    messages = [HumanMessage(content=query)]
    response = model_with_tools.invoke(messages)
    
    # Add model's response to the conversation history
    messages.append(response)
    
    # 4. Check if the model decided to call a tool.
    if response.tool_calls:
        print("\n[Model Response]: The model decided to call a tool!")
        for tool_call in response.tool_calls:
            print(f" -> Calling Tool: '{tool_call['name']}' with args: {tool_call['args']}")
            
            # Execute the tool locally
            if tool_call['name'] == 'get_weather':
                tool_output = get_weather.invoke(tool_call['args'])
                print(f" -> Tool Output: '{tool_output}'")
                
                # Append the tool execution result back to the message history.
                messages.append(
                    ToolMessage(
                        content=str(tool_output),
                        tool_call_id=tool_call['id']
                    )
                )
        
        # 5. Send the entire conversation history back to OpenAI for final answer.
        print("\n5. Sending tool results back to OpenAI for final answer...")
        final_response = model_with_tools.invoke(messages)
        print("\nFinal Response:")
        print(final_response.content)
    else:
        print("\n[Model Response]: The model answered directly without using any tools:")
        print(response.content)

if __name__ == "__main__":
    main()
