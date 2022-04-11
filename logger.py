import logging
import os


LEVELS = {
    "debug": logging.DEBUG,
    "info": logging.INFO,
    "warning": logging.WARNING,
    "error": logging.ERROR,
    "critical": logging.CRITICAL,
    None: logging.NOTSET
}


class LoggerSetup:
    def __init__(self, level="debug") -> None:
        logging.root.setLevel(LEVELS[level])

    def get_minimal(self, name):
        """Simple logger"""
        # Creating handler
        handler = logging.StreamHandler()

        # Create formatters and add it to handlers
        s_format = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(message)s")
        handler.setFormatter(s_format)

        return self.create_logger(name=name, handler=handler)

    def get_detailed(self, name):
        """Getting detailed logger.
        Usually used for debug & error levels."""
        # Create handler
        handler = logging.StreamHandler()

        # Create formatters and add it to handlers
        s_format = logging.Formatter(
            "%(asctime)s - %(levelname)s - %(name)s - %(filename)s - %(lineno)d - %(message)s")
        handler.setFormatter(s_format)

        return self.create_logger(name=name, handler=handler)

    def file_log(self, name, file_path):
        """Logging into a file"""
        # Create handler
        f_handler = logging.FileHandler(file_path)

        # Create formatters and add it to handlers
        f_format = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s')
        f_handler.setFormatter(f_format)

        return self.create_logger(name=name, handler=f_handler)

    def create_logger(self, name, handler):
        logger = logging.getLogger(name)
        logger.addHandler(handler)
        return logger


LOGGER_SETUP = LoggerSetup(level=os.getenv("LOG_LEVEL"))
