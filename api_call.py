import json
import os
import requests
from dotenv import load_dotenv
from pathlib import Path

from IPython.display import display, Markdown

def chat_with_openrouter(prompt, model="deepseek/deepseek-r1-0528:free"):
    """
    Send a chat completion request to OpenRouter API
    
    Args:
        prompt (str): The user's prompt/question
        model (str): The model to use for completion
        
    Returns:
        dict: The API response
    """
    # Set OpenRouter API key
    project_root = Path(__file__).parent if '__file__' in globals() else Path.cwd()
    env_path = project_root / '.env'
    load_dotenv(dotenv_path=env_path)

    api_key = os.getenv("OPENROUTER_API_KEY")
    if not api_key:
        raise ValueError("OPENROUTER_API_KEY not set in .env file.")
        
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    
    data = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }
    
    response = requests.post(
        "https://openrouter.ai/api/v1/chat/completions",
        headers=headers,
        json=data
    )
    
    return response.json() # ["choices"][0]["message"]["content"]


# Example usage - you can run this in a cell
user_prompt = "The course is already started. Can I still join the course?"
response = chat_with_openrouter(user_prompt)

# Display the full response in a nicely formatted way
# display(Markdown("## Full API Response"))
# display(Markdown("```json\n" + json.dumps(response, indent=2) + "\n```"))

# # Extract and display just the model's response
# try:
#     assistant_message = response["choices"][0]["message"]["content"]
#     display(Markdown("## Model's Response"))
#     display(Markdown(assistant_message))
# except (KeyError, IndexError) as e:
#     display(Markdown(f"**Error extracting response**: {e}"))
#     display(Markdown(f"Full response: {response}"))

print(response)

