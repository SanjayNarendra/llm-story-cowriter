import os
from utils.json_loader import load_json
from utils.logger import logger


def load_prompt(prompt_name: str) -> dict:
    try:
        filepath = os.path.join("prompts", f"{prompt_name}.json")
        prompt = load_json(filepath)
        logger.info(f"Loaded prompt: {prompt_name}")
        return prompt

    except Exception as e:
        logger.error(f"Error loading prompt: {e}")
        return {}