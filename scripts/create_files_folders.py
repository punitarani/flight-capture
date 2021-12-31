from pathlib import Path

from defs import SYSTEM_LOG, CONFIG_JSON
from defs import TEMP, LOGS
from src.loggers import SystemLogger


def create_files_folders():
    """
    Create Necessary Files and Folders
    """

    # Initialize logger
    logger = SystemLogger("system").logger

    # Initial log
    logger.info("Creating necessary files and folders...")

    """
    Create Folders
        /logs
        /temp
    """
    folders = [LOGS, TEMP]

    for folder in folders:
        # Convert folder to Path object
        if isinstance(folder, str):
            folder = Path(folder)

        if folder.exists():
            logger.info(f"Folder {folder} already exists")
        else:
            folder.mkdir(parents=True)
            logger.info(f"Created folder {folder}")

    """
    Create Files
        /logs/system.log
        /config/config.json
    """
    files = [SYSTEM_LOG, CONFIG_JSON]

    for file in files:
        # Convert file to Path object
        if isinstance(file, str):
            file = Path(file)

        if file.exists():
            logger.info(f"File {file} already exists")
        else:
            file.touch()
            logger.info(f"Created file {file}")


if __name__ == "__main__":
    create_files_folders()
