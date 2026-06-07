
import os
from dotenv import load_dotenv
from google import genai
import argparse
from google.genai import types
from prompts import system_prompt

def main():
    #print("Hello from ai-agent!")
    # begin code
    # parser object
    parser = argparse.ArgumentParser(description="Chat bot")
    parser.add_argument("prompt", type=str, help="prompt give genAI  a string")
    parser.add_argument("--verbose", action="store_true", help="Enable verbose output")
    # get arguments
    args = parser.parse_args()

    # load .env file into environment to access api key
    load_dotenv()

    api_key = os.environ.get("GEMINI_API_KEY")
    # check for if key exists
    if api_key is None:
        raise RuntimeError("api key not found")
    # chat bot interaction
    client = genai.Client(api_key=api_key)
# chat history container
    messages: list[types.Content] = [
        types.Content(role="user", parts=[types.Part(text=args.prompt)])
    ]
    response = client.models.generate_content(model="gemini-2.5-flash", contents=messages, config=types.GenerateContentConfig(system_instruction=system_prompt))
    if response.usage_metadata is None:
        raise RuntimeError("metadata not found")
    
    if args.verbose:
        print(f"User prompt: {args.prompt}")
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
        print(response.text)
    else:
        print(response.text)


if __name__ == "__main__":
    main()
