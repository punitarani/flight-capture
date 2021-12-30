import json
from pathlib import Path

# Path data
CURRENT_DIR = Path(__file__).parent.absolute()
CONFIG_PATH = Path.joinpath(CURRENT_DIR, 'config.json')


# Load config
with open(CONFIG_PATH, 'r') as config_file:
    config_data = json.load(config_file)

    # Location
    latitude = config_data['location']['latitude']
    longitude = config_data['location']['longitude']
    altitude = config_data['location']['altitude']

    # OpenSky
    opensky_username = config_data['opensky']['username']
    opensky_password = config_data['opensky']['password']


if __name__ == '__main__':
    print(latitude)
    print(longitude)
    print(altitude)
    print(opensky_username)
    print(opensky_password)
