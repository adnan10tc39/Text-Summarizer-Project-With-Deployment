import os
import sys
import logging

logging_str = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]" #ye loggin string different hai us logging string say jo hum ny template.py mien use ki thi us mien sirf time of message dekha rahy thy lakin eder module  aur additional cheezien b log mien dekhaien gy.
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir, exist_ok=True)



logging.basicConfig(
    level= logging.INFO,
    format= logging_str,

    handlers=[
        logging.FileHandler(log_filepath), #FileHandler store the logs in or log file within log directory
        logging.StreamHandler(sys.stdout) #streamhandler shows logs in our terminal
    ]
)

logger = logging.getLogger("textSummarizerLogger")