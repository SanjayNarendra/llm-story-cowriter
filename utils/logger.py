import logging 
import os
import sys

log_dir = 'logs'
log_filepath = os.path.join(log_dir, 'llm_writer.log')
log_format = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"

# create log directory
os.makedirs(log_dir, exist_ok=True)

# logger setup
logging.basicConfig(
    level=logging.INFO,
    format=log_format,
    
    handlers=[
        logging.FileHandler(log_filepath),
        logging.StreamHandler(sys.stdout)
    ]
)

logger = logging.getLogger('llm_logger')