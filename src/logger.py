import logging
import os
from datetime import datetime

# Print the current working directory for debugging purposes
print(f"Current working directory: {os.getcwd()}")

# Create a log file name
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Define the directory for log files
logs_dir = os.path.join(os.getcwd(), "logs")
os.makedirs(logs_dir, exist_ok=True)

# Define the full log file path
LOG_FILE_PATH = os.path.join(logs_dir, LOG_FILE)

# Print the log file path for debugging purposes
print(f"Log file path: {LOG_FILE_PATH}")

# Configure logging
logging.basicConfig(
    filename=LOG_FILE_PATH,
    format="[ %(asctime)s ] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

if __name__ == '__main__':
    logging.info('Logging has started')
    print("Logging has started")
