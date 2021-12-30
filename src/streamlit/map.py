import pandas as pd
import streamlit as st

from src.flights import Flights


class Map:
    """
    Map Flight Data
    """
    def __init__(self):
        """
        Initialize Map Class
        """
        self.Flights = Flights()
        self.flights_df = self.Flights.flights

        self.home_df = self.create_home_df()

    def __call__(self, *args, **kwargs):
        """
        Run map function when Map class is called
        """
        self.map()

    def update_data(self):
        """
        Update flight data
        """
        self.Flights = Flights()
        self.flights_df = self.Flights.flights

    def create_home_df(self):
        """
        Create home location dataframe
        """
        data = {"location": ["home"],
                "latitude": [self.Flights.reference_latitude],
                "longitude": [self.Flights.reference_longitude]}

        df = pd.DataFrame(data)

        return df

    def map(self):
        """
        Map flight data
        """
        st.map(self.flights_df)

    def map_home(self):
        """
        Map home location
        """
        st.map(self.home_df)

    def map_refresh(self):
        """
        Map and constantly update flight data
        """
        with st.empty():
            while True:
                self.update_data()
                st.map(self.flights_df)
