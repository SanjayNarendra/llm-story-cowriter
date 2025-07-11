import json
from utils.logger import logger

def load_json(filepath: str) -> dict:
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            data = json.load(f)
        logger.info(f'successfully loaded JSON from: {filepath}')
        return data
    
    except FileNotFoundError:
        logger.error(f'File not found: {filepath}')
        raise
    except json.JSONDecodeError as e:
        logger.error(f'JSON decode error in {filepath}: {e}')
        raise