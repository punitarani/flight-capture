import json
from pathlib import Path

# Path data
CURRENT_DIR = Path(__file__).parent.absolute()
CONFIG_PATH = Path.joinpath(CURRENT_DIR, 'config.json')


# Load config
with open(CONFIG_PATH, 'r') as config_file:
    config_data = json.load(config_file)

    # Location
    latitude = float(config_data['location']['latitude'])
    longitude = float(config_data['location']['longitude'])
    altitude = float(config_data['location']['altitude'])

    # OpenSky
    opensky_username = config_data['opensky']['username']
    opensky_password = config_data['opensky']['password']

    # MapBox
    mapbox_token = config_data['streamlit']['mapbox_token']


if __name__ == '__main__':
    print("latitude:            ", latitude)
    print("longitude:           ", longitude)
    print("altitude:            ", altitude)
    print("opensky_username:    ", opensky_username)
    print("opensky_password:    ", opensky_password)
    print("mapbox_token:        ", mapbox_token)
