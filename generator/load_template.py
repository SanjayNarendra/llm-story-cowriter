import os
from utils.json_loader import load_json
from utils.logger import logger

template_dir = os.path.join('templates')

def load_template(name: str) -> dict:
    filepath = os.path.join('templates', f'{name}.json')
    logger.info(f'Loading template:, {filepath}')
    return load_json(filepath)
