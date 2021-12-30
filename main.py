from opensky import OpenSkyApi
from config.config import opensky_username, opensky_password

if __name__ == '__main__':
    api = OpenSkyApi(username=opensky_username, password=opensky_password)
    states = api.get_states()
    for s in states.states:
        print("(%r, %r, %r, %r)" % (s.reference_longitude, s.reference_latitude, s.baro_altitude, s.velocity))
