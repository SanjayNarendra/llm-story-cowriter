from templates.template_loader import load_all_templates
from utils.logger import logger


def load_template(template_name: str) -> dict:
    """
    Loads a specific template configuration by its name from the template registry

    Args:
        template_name (str): The name of the template file (without .json)

    Returns:
        dict: Parsed  template content dictionary if found, else empty dict
    """
    try:
        all_templates = load_all_templates()
        if template_name in all_templates:
            logger.debug(f"Loaded template: {template_name}")
            return all_templates[template_name]
        else:
            logger.warning(f"Template '{template_name}' not found in registry.")
            return {}

    except Exception as e:
        logger.error(f"Failed to load template '{template_name}': {e}")
        return {}
