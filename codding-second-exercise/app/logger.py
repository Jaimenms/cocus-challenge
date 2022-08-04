import os
import logging.config

# Reading the logging configuration file
LOGGING_CONFIG_FILE = os.getenv("LOGGING_CONFIG_FILE", "./logging.conf")

if os.path.exists(LOGGING_CONFIG_FILE):
    logging.config.fileConfig(LOGGING_CONFIG_FILE)


def get_logger(name="app"):
    """
    Function to get the logger
    :param name: name of the logger
    :return:
    """

    logger = logging.getLogger(name)

    # If DEBUG mode
    if os.getenv("DEBUG", "False") == "True":
        logger.setLevel("DEBUG")

    return logger
