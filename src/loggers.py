# Configuring all Loggers

import logging
import sys
from pathlib import Path

from defs import SYSTEM_LOG

# Dict of all instantiated loggers
loggers = {}


class SystemLogger:
    """
    Main System Logger
    """
    def __init__(self, logger_name: str, add_file_handler: bool = True, add_stream_handler: bool = True):
        """
        Initialize System Logger
        """
        self.logger_name = logger_name

        # If logger exists, return existing logger
        if loggers.get(self.logger_name):
            self.logger = loggers.get(self.logger_name)

        # Otherwise create new logger
        else:
            # input params
            self.add_file_handler = add_file_handler
            self.add_stream_handler = add_stream_handler

            # Define log formatter
            self.formatter = logging.Formatter('%(asctime)s | %(name)s | %(levelname)s | %(message)s')

            # Define handlers
            self.file_handler = logging.FileHandler(SYSTEM_LOG, mode='a')
            self.file_handler.setFormatter(self.formatter)
            self.stream_handler = logging.StreamHandler(sys.stdout)
            self.stream_handler.setFormatter(self.formatter)

            # Create log file if it doesn't exist
            if not Path(SYSTEM_LOG).is_file():
                self.createLog()

            # Get logger
            self.logger = self.getLogger()

            # Set default logging level to DEBUG
            self.logger.setLevel(logging.DEBUG)

            # Save to loggers dict
            loggers[self.logger_name] = self.logger

    def getLogger(self) -> logging.Logger:
        """
        Get logger
        """
        logger = logging.getLogger(name=self.logger_name)
        self.addHandlers(logger)
        return logger

    def addHandlers(self, logger: logging.Logger) -> logging.Logger:
        """
        Add handlers to logger
        :param logger: Logger to add handlers to
        """

        # Add handler iff logger is parent (i.e. not child) and requested
        if ("." not in self.logger_name) and self.add_file_handler:
            logger.addHandler(self.file_handler)

        if ("." not in self.logger_name) and self.add_stream_handler:
            logger.addHandler(self.stream_handler)

        return logger

    @staticmethod
    def createLog():
        """
        Create log file
        """
        Path(SYSTEM_LOG).touch()
