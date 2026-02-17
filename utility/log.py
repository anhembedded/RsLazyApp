import logging
import csv
import os
import inspect


class ColorFormatter(logging.Formatter):
    """Custom formatter to add colors to console logs."""
    COLORS = {
        logging.DEBUG: "\033[32m",    # Green
        logging.INFO: "\033[34m",     # Blue
        logging.WARNING: "\033[33m",  # Yellow
        logging.ERROR: "\033[31m",    # Red
        logging.CRITICAL: "\033[41m", # Red Background
    }
    RESET = "\033[0m"

    def format(self, record):
        log_color = self.COLORS.get(record.levelno, self.RESET)
        
        # Format timestamp
        timestamp = self.formatTime(record, self.datefmt)
        
        # Split the custom formatted message (path:line,message)
        try:
            path_info, actual_message = record.msg.split(',', 1)
            # Shorten path to relative for better readability
            rel_path = os.path.relpath(path_info, os.getcwd())
            path_display = f"{rel_path}"
        except ValueError:
            path_display = "unknown:0"
            actual_message = record.msg

        # Final string construction with alignment
        levelname = f"[{record.levelname}]".ljust(10)
        return (f"{timestamp} {log_color}{levelname}{self.RESET} "
                f"\033[90m({path_display})\033[0m {actual_message}")

class Logger_T:
    def __init__(self, log_file='log/LazyApp_Log.csv'):
        # Ensure log directory exists
        os.makedirs(os.path.dirname(log_file), exist_ok=True)
        self.log_file = log_file
        self._setup_logger()

    def _setup_logger(self):
        """Sets up the logging configuration."""
        self.logger = logging.getLogger("LazyAppLogger")
        self.logger.setLevel(logging.DEBUG)

        # Ensure log file exists with headers
        if not os.path.exists(self.log_file):
            with open(self.log_file, 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Timestamp", "Level", "File:Line", "Message"])

        # File handler (CSV format) - Keep it simple/standard
        file_handler = logging.FileHandler(self.log_file, mode='a', encoding='utf-8')
        file_formatter = logging.Formatter('%(asctime)s,%(levelname)s,%(message)s',
                                           datefmt='%Y-%m-%d %H:%M:%S')
        file_handler.setFormatter(file_formatter)
        file_handler.setLevel(logging.DEBUG)

        # Console handler (Colored & Professional)
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(ColorFormatter(datefmt='%H:%M:%S'))
        console_handler.setLevel(logging.DEBUG)

        # Add handlers
        if not self.logger.hasHandlers():
            self.logger.addHandler(file_handler)
            self.logger.addHandler(console_handler)

    def log(self, message, level=logging.INFO):
        """Logs a message with the given level."""
        frame = inspect.currentframe().f_back
        abs_path = os.path.abspath(frame.f_code.co_filename)
        line_number = frame.f_lineno

        # Pass combined info to record.msg
        formatted_info = f"{abs_path}:{line_number},{message}"
        self.logger.log(level, formatted_info)




# Example usage
logger = Logger_T()
if __name__ == "__main__":
    logger.log(message="Initializing UI", level=logging.INFO)
    logger.log(message="Loading configurations", level=logging.DEBUG)
    logger.log(message="UI started successfully", level=logging.WARNING)


