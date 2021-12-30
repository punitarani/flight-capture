import os

from src.loggers import SystemLogger


def install_requirements():
    logger = SystemLogger("system").logger

    try:
        logger.info("Installing required libraries")
        os.system("pip install -r requirements.txt")
        logger.info("Successfully installed required libraries")
    except Exception as err:
        logger.error(f"Error installing required libraries. Error: {err}")


if __name__ == "__main__":
    install_requirements()
