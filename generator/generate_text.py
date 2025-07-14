import requests
import os
from dotenv import load_dotenv
from utils.logger import logger

# Load environment variables
load_dotenv()
MODEL_NAME = os.environ.get('MODEL_NAME')
OLLAMA_API = os.environ.get('OLLAMA_API')

def generate_text(prompt_config: dict, story_text: str) -> str:
    """
    Sends a prompt to the local LLM API (Ollama) and retrieves a generated response.

    Args:
        prompt_config (dict): The JSON-loaded configuration with template and actions
        story_text (str): The user’s current story text or selected input

    Returns:
        str: LLM-generated continuation of the story
    """
    try:
        template = prompt_config['actions'][0]['template']

        filled_prompt = template.replace('::full::', story_text)

        response = requests.post(
            OLLAMA_API,
            json={'model': MODEL_NAME, 'prompt': filled_prompt, 'stream': False}
        )
        response.raise_for_status()
        
        generated = response.json()['response']
        logger.info('LLM response generated successfully')
        return generated

    except Exception as e:
        logger.error(f'Error generating text: {e}')
        return '[Error: Unable to generate text]'