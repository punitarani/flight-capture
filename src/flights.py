# Filter flights based on location and get additional flight relevant information

from math import sin, cos, sqrt, atan2, radians, degrees

from config.config import longitude, latitude, altitude, opensky_username, opensky_password
from opensky import OpenSkyApi


class Flights:
    """
    Class to filter Flights based on location
    """

    def __init__(self, offset: float = 0.5):
        """
        Initialize the class
        :param offset: The offset from the reference point's coordinates in x and y
        """

        # Create an instance of the OpenSky API with user credentials
        self.opensky = OpenSkyApi(username=opensky_username, password=opensky_password)

        # Initialize the reference point
        self.reference_longitude = longitude
        self.reference_latitude = latitude
        self.reference_altitude = altitude

        # Get the bounding box based on the reference point
        self.bbox_offset = offset
        self.bbox = self.get_bbox(offset=self.bbox_offset)

        # Get the list of flights in the bounding box
        self.flights = self.opensky.get_states_df(bbox=self.bbox)

        # Add the distance and rank flights based on distance
        self.add_distance(rank=True)

    def get_bbox(self, offset: float = 0.5) -> tuple:
        """
        Get the bounding box for the reference point
        :param offset: The offset from the reference point's coordinates
        :return: The bounding box coordinates tuple (min_latitude, max_latitude, min_longitude, max_latitude)
        """

        bbox = (self.reference_latitude - offset, self.reference_latitude + offset, self.reference_longitude - offset,
                self.reference_longitude + offset)
        return bbox

    @staticmethod
    def calculate_distance(lat1, lon1, lat2, lon2):
        """
        Calculate the distance between two coordinate points
        """

        R = 6370  # Radius of the earth in km

        # Convert reference_latitude and reference_longitude to radians
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        # Haversine formula
        dlon = lon2 - lon1
        dlat = lat2 - lat1

        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c

        return distance

    def get_distance(self):
        """
        Get the distance between the reference point and the flight
        """

        distances = {}

        for flight in self.flights.index.tolist():
            flight_data = self.flights.loc[flight]

            # Calculate the distance between the reference point and the flight
            distance = self.calculate_distance(lat1=flight_data.loc['latitude'],
                                               lon1=flight_data.loc['longitude'],
                                               lat2=self.reference_latitude,
                                               lon2=self.reference_longitude)

            distances.update({flight: distance})

        return distances

    def add_distance(self, rank: bool = True):
        """
        Add the distance to the flights dataframe
        """

        self.flights['distance'] = self.get_distance().values()

        if rank:
            self.flights = self.flights.sort_values(by='distance', ascending=True)

        return self.flights

    ####################################################################################################################
    @staticmethod
    def get_direction(lat1, lon1, lat2, lon2):
        """
        Calculate the direction between two coordinate points
        """

        # Convert reference_latitude and reference_longitude to radians
        lat1 = radians(lat1)
        lon1 = radians(lon1)
        lat2 = radians(lat2)
        lon2 = radians(lon2)

        # Haversine formula
        dlon = lon2 - lon1
        y = sin(dlon) * cos(lat2)
        x = cos(lat1) * sin(lat2) - sin(lat1) * cos(lat2) * cos(dlon)
        bearing = atan2(y, x)

        return bearing

    @staticmethod
    def get_angle(flight_distance, flight_altitude):
        """
        Calculate the angle between the flight and the reference point
        """

        # Calculate the angle between the flight and the reference point
        # flight distance is in km, so convert to meters
        angle = atan2(flight_altitude, flight_distance*1000)

        return angle

    def find_plane(self, icao24: str):
        """
        Gets the direction and angle to look at to find the plane
        """

        # Get the flight data from the flights dataframe based on the icao24
        flight_data = self.flights.loc[icao24]

        # Calculate the direction between the reference point and the flight
        direction = self.get_direction(lat1=self.reference_latitude,
                                       lon1=self.reference_longitude,
                                       lat2=flight_data.loc['latitude'],
                                       lon2=flight_data.loc['longitude'])

        # Calculate the angle between the flight and the reference point
        angle = self.get_angle(flight_distance=flight_data.loc['distance'],
                               flight_altitude=flight_data.loc['geo_altitude'])

        return degrees(direction), degrees(angle)


if __name__ == "__main__":
    from tabulate import tabulate

    flights = Flights()

    _flights_data_df = flights.flights
    _flights_data_df_cols = _flights_data_df

    print(tabulate(_flights_data_df, _flights_data_df_cols, tablefmt='simple'))

    # Closest:
    _complete = False
    _flight_index = 0
    while not _complete:
        try:
            closest_flight = _flights_data_df.index.tolist()[_flight_index]
            print(flights.find_plane(closest_flight))
            _complete = True
        except Exception as err:
            print(err)
            _flight_index += 1
