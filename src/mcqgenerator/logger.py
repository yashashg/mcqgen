import logging
import os
from datetime import datetime

LOG_FILE = f"mcq_generator_{datetime.now().strftime('%Y%m%d_%H%M%S')}.log"

log_path = os.path.join(os.getcwd(), LOG_FILE)
 
os.makedirs(log_path,exist_ok=True)

log_path_file = os.path.join(log_path, LOG_FILE)

logging.basicConfig(level=logging.INFO,filename=log_path_file, filemode='w',format='%(asctime)s - %(levelname)s - %(message)s')
