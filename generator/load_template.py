import os
from utils.json_loader import load_json
from utils.logger import logger


template_dir = os.path.join('templates')

def load_template(template_name: str) -> dict:
    try:
        filepath = os.path.join('templates', f'{template_name}.json')
        template = load_json(filepath)
        logger.info(f'Loading template:, {filepath}')
        return template
        
    except Exception as e:
       logger.error(f"Error loading template '{template_name}': {e}")
       return {}
