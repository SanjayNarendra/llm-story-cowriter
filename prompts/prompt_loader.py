import os
from utils.json_loader import load_json
from utils.logger import logger


def load_all_prompts(prompt_dir='prompts') -> dict:
    """
    Load all JSON prompt files from the given directory

    Args:
        prompt_dir (str): Directory path containing prompt JSON files (default is 'prompts')

    Returns:
        dict: Mapping of prompt names (filename without .json) to their parsed JSON content
    """
    prompts = {}

    try:
        for filename in os.listdir(prompt_dir):
            if filename.endswith(".json"):
                prompt_name = os.path.splitext(filename)[0]
                filepath = os.path.join(prompt_dir, filename)
                prompts[prompt_name] = load_json(filepath)
                logger.debug(f"Loading prompt: {filename}")
        return prompts

    except Exception as e:
        logger.error(f'Failed to load prompts from {prompt_dir}: {e}')
        return {}