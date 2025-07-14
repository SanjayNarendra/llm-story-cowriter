"""
Module: action_handler
Handles different prompt action types such as 'generate', 'static', 'options', and 'generate-options'.
"""

from generator.generate_text import generate_text
from utils.logger import logger


def handle_action(action: dict, story_text: str, prompt_config: dict) -> str:
    """
    Process a single action based on its type and return the result

    Args:
        action (dict): The action definition from the prompt config
        story_text (str): The current story input from the user
        prompt_config (dict): The full prompt configuration, in case metadata is needed

    Returns:
        str: Resulting text from the action (LLM response, static text, etc.)
    """
    try:
        action_type = action.get("type")

        if action_type == "generate":
            return generate_text(prompt_config, story_text)

    except Exception as e:
        logger.error(f"Failed to handle action: {e}")
        return "[Error: Action handling failed]"
