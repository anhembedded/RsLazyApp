import logging
import csv
import os
import inspect


class Logger_T:
    def __init__(self, log_file='log/LazyApp_Log.csv'):
        self.log_file = log_file
        self._setup_logger()


    def _setup_logger(self):
        """Sets up the logging configuration."""
        self.logger = logging.getLogger("LazyAppLogger")
        self.logger.setLevel(logging.DEBUG)  # Log everything from DEBUG and above


        # Ensure log file exists with headers
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Level", "File:Line", "Message"])


        # File handler (CSV format)
        file_handler = logging.FileHandler(self.log_file, mode='a', encoding='utf-8')
        file_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)


        # Console handler
        console_handler = logging.StreamHandler()
        console_formatter = logging.Formatter('%(asctime)s [%(levelname)s] %(message)s')
        console_handler.setFormatter(console_formatter)
        console_handler.setLevel(logging.DEBUG)


        # Add handlers to logger (prevent duplicate handlers)
        if not self.logger.hasHandlers():
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)


    def log(self, message, level=logging.INFO):
        """Logs a message with the given level."""
        frame = inspect.currentframe().f_back  # Get caller frame
        abs_path = os.path.abspath(frame.f_code.co_filename)  # Get absolute file path
        line_number = frame.f_lineno  # Get line number


        # Manually format message to include absolute path
        formatted_message = f"{abs_path}:{line_number},{message}"
        self.logger.log(level, formatted_message)




# Example usage
logger = Logger_T()
if __name__ == "__main__":
    logger.log(message="Initializing UI", level=logging.INFO)
    logger.log(message="Loading configurations", level=logging.DEBUG)
    logger.log(message="UI started successfully", level=logging.WARNING)


