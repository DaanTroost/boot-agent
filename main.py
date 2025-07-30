import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types
from available_function import available_functions
import config

def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    client = genai.Client(api_key=api_key)
    user_prompt = sys.argv[1]
    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents = messages,
        config=types.GenerateContentConfig(system_instruction=config.system_prompt, tools=[available_functions])
    )

    print(response.text)
    for function_call in response.function_calls:
        print(f"Calling function: {function_call.name}({function_call.args})")
    if "--verbose" in sys.argv:
        print(f"User prompt: {user_prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}" + 
          f"\nResponse tokens: {response.usage_metadata.candidates_token_count}")
    


if __name__ == "__main__":
    main()
