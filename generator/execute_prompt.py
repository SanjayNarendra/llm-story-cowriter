"""
Module: execute_prompt
Executes a given prompt configuration by processing all defined actions.
"""

from generator.action_handler import handle_action
from utils.logger import logger


def execute_prompt(prompt_config: dict, story_text: str) -> str:
    """
    Execute the given prompt configuration and return the result

    Args:
        prompt_config (dict): Full prompt configuration containing 'actions'
        story_text (str): Current state of the user’s story input.

    Returns:
        str: Resulting response after processing prompt actions.
    """
    try:
        actions = prompt_config.get("actions", [])

        if not actions:
            logger.warning("Prompt config has no actions defined.")
            return "[No actions defined in prompt]"

        results = []

        for action in actions:
            output = handle_action(action, story_text, prompt_config)
            results.append(output)

        return "\n".join(results).strip()

    except Exception as e:
        logger.error(f"Failed to execute prompt: {e}")
        return "[Error executing prompt]"
