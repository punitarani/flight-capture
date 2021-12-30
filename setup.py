from scripts import create_files_folders, create_config_json, install_requirements


if __name__ == "__main__":
    create_files_folders.create_files_folders()
    create_config_json.create_config_json(overwrite=True)
    install_requirements.install_requirements()
