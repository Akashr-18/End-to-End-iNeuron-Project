import logging
import os
import sys
from datetime import datetime

logging_str ="[%(asctime)s]:  %(lineno)d: %(levelname)s: %(module)s: %(message)s"

LOG_FILE=f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

log_path=os.path.join(os.getcwd(),"logs")
os.makedirs(log_path,exist_ok=True)

log_filepath=os.path.join(log_path,LOG_FILE)

logging.basicConfig(
    level = logging.INFO,
    format = logging_str,
    handlers = [
        logging.StreamHandler(sys.stdout),
        logging.FileHandler(log_filepath)
        ]
)

logger = logging.getLogger('EndtoEndLogger')