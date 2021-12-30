# Script to create config.json file from config_template.json

import json
from pathlib import Path

from src.loggers import SystemLogger
from defs import CONFIG_JSON, CONFIG_TEMPLATE_JSON


# Create config.json file from config_template.json Path objects
CONFIG = Path(CONFIG_JSON)
CONFIG_TEMPLATE = Path(CONFIG_TEMPLATE_JSON)


def create_config_json(overwrite: bool = False) -> dict:
    """
    Create config.json file from config_template.json with user input
    """
    logger = SystemLogger("system").logger

    config = {}
    overwriting = False

    # Check if config.json exists and if overwrite is True
    if CONFIG.exists() and not overwrite:
        logger.info("config.json file already exists. Not overwriting config.json.")
        return config
    elif CONFIG.exists() and overwrite:
        logger.info("config.json file already exists.")
        overwriting = True
    else:
        logger.info("Creating new config.json file from user input.")

    # Confirm overwrite
    if overwriting:
        overwrite = input("Are you sure you want to overwrite config.json? (y/n): ")
        if overwrite.lower() != "y":
            logger.info("Not overwriting config.json")
            return config

    # Get user config details from config_template fields and store in config dict
    with open(CONFIG_TEMPLATE, "r") as template_file:
        template = json.load(template_file)

        # Iterate through config sections
        for section_name in template.keys():
            section = template[section_name]
            section_data = {}

            #
            if section_name == "location":
                print("\nEnter 'home' coordinates:")
                print("Can be found at https://gps-coordinates.org/")

            # Iterate through fields in section
            for field in section.keys():
                # Get user input
                field_input = input(f"{field} ({section_name}): ")

                # Update section data with user input
                section_data.update({field: field_input})

            # Update config with section data
            config.update({section_name: section_data})

    # Write config dict to config.json file
    with open(CONFIG, "w") as config_file:
        json.dump(config, config_file, indent=4)

    # Log success
    if not overwriting:
        logger.info("Successfully created config.json file")
    else:
        logger.info("Successfully overwrote config.json file")

    return config


if __name__ == "__main__":
    create_config_json(overwrite=True)
