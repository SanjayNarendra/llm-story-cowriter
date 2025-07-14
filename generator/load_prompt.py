from prompts.prompt_loader import load_all_prompts
from utils.logger import logger


def load_prompt(prompt_name: str) -> dict:
    """
    Loads a specific prompt configuration by its name from the prompt registry.

    Args:
        prompt_name (str): The name of the prompt file (without .json)

    Returns:
        dict: Parsed prompt configuration dictionary if found, else empty dict
    """
    try:
        all_prompts = load_all_prompts()
        if prompt_name in all_prompts:
            logger.debug(f"Loaded prompt: {prompt_name}")
            return all_prompts[prompt_name]
        else:
            logger.warning(f"Prompt '{prompt_name}' not found in registry.")
            return {}
        
    except Exception as e:
        logger.error(f"Failed to load prompt '{prompt_name}': {e}")
        return {}