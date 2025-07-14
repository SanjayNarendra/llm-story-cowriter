import os
from utils.json_loader import load_json
from utils.logger import logger


def load_all_templates(template_dir='templates') -> dict:
    """
    Load all JSON files from the given directory

    Args:
        template_dir (str): Path to the templates directory (default is 'templates')

    Returns:
        dict: Mapping of template names (filename without .json) to their parsed JSON content
    """
    templates = {}

    try:
        for filename in os.listdir(template_dir):
            if filename.endswith('.json'):
                template_name = os.path.splitext(filename)[0]
                filepath = os.path.join(template_dir, filename)
                templates[template_name] = load_json(filepath)
                logger.debug(f"Loaded template: {template_name}")
        return templates
    
    except Exception as e:
        logger.error(f"Failed to load templates from {template_dir}: {e}")
        return {}
