import logging
import traceback
from logging.handlers import RotatingFileHandler

class Logger:
    """
    A class to encapsulate the logging setup and provide utilities for logging
    messages and debugging information.

    Attributes:
    logger (logging.Logger): The root logger instance.
    """

    def __init__(self, name: str, log_file: str = None, log_level: int = logging.DEBUG):
        """
        Initializes the Logger instance.

        Args:
            name (str): The name of the logger.
            log_file (str, optional): The file to log messages to. Defaults to None.
            log_level (int, optional): The logging level. Defaults to logging.DEBUG.
        """
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        
        # Console handler
        console_handler = logging.StreamHandler()
        console_handler.setFormatter(formatter)
        self.logger.addHandler(console_handler)
        
        # File handler
        if log_file:
            file_handler = RotatingFileHandler(log_file, maxBytes=10485760, backupCount=5)
            file_handler.setFormatter(formatter)
            self.logger.addHandler(file_handler)
    
    def debug(self, msg: str):
        """
        Logs a debug message.

        Args:
            msg (str): The message to log.
        """
        self.logger.debug(msg)
    
    def info(self, msg: str):
        """
        Logs an informational message.

        Args:
            msg (str): The message to log.
        """
        self.logger.info(msg)
    
    def warning(self, msg: str):
        """
        Logs a warning message.

        Args:
            msg (str): The message to log.
        """
        self.logger.warning(msg)
    
    def error(self, msg: str):
        """
        Logs an error message.

        Args:
            msg (str): The message to log.
        """
        self.logger.error(msg)
    
    def critical(self, msg: str):
        """
        Logs a critical message.

        Args:
            msg (str): The message to log.
        """
        self.logger.critical(msg)
    
    def log_exception(self, exc: Exception):
        """
        Logs an exception with the stack trace.

        Args:
            exc (Exception): The exception to log.
        """
        self.logger.error(f"Exception occurred: {exc}")
        self.logger.error(traceback.format_exc())

if __name__ == "__main__":
    # Example usage
    logger = Logger("MyLogger", log_file="app.log", log_level=logging.DEBUG)
    try:
        logger.debug("This is a debug message")
        logger.info("This is an info message")
        logger.warning("This is a warning message")
        logger.error("This is an error message")
        logger.critical("This is a critical message")
        
        # Simulate an exception
        1 / 0
    except Exception as e:
        logger.log_exception(e)