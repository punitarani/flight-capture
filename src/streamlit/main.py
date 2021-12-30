# Streamlit Main File

import streamlit as st
from src.streamlit.map import Map


class Main:
    """
    Streamlit Main Class
    """

    def __init__(self):
        """
        Constructor
        """
        st.set_page_config(page_title="Flight Capture",
                           page_icon="✈",
                           layout="wide")

    @staticmethod
    def main():
        """
        Main Page
        """
        st.title("Flight Capture")

        # Add Map of nearby flights (Refreshes every ~1 seconds)
        Map().map_refresh()
