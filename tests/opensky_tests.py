import time
import unittest
from datetime import datetime
from unittest import TestCase, skipIf

from opensky import OpenSkyApi, StateVector

from config.config import opensky_username, opensky_password

# Add your username, password and at least one sensor
# to run all tests
TEST_USERNAME = "" #opensky_username
TEST_PASSWORD = "" #opensky_password
TEST_SERIAL = []


class TestOpenSkyApi(TestCase):
    def setUp(self):
        if len(TEST_USERNAME) > 0:
            self.api = OpenSkyApi(username=TEST_USERNAME, password=TEST_PASSWORD)
        else:
            self.api = OpenSkyApi()

    def test_get_states(self):
        r = self.api.get_states()
        print(r)
        self.assertGreater(len(r["states"]), 0, "Retrieve at least one State Vector")

    def test_get_states_rate_limit(self):
        r = self.api.get_states()
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")
        r = self.api.get_states()
        self.assertIsNone(r, "Rate limit produces 'None' result")

    def test_get_states_time(self):
        now = int(time.time())
        r = self.api.get_states(time_secs=now)
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")

    def test_get_states_datetime(self):
        r = self.api.get_states(time_secs=datetime.now())
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")

    def test_get_states_bbox(self):
        r = self.api.get_states(bbox=(45.8389, 47.8229, 5.9962, 10.5226))
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")

    def test_get_states_bbox_err(self):
        with self.assertRaisesRegexp(ValueError, "Invalid bounding box!.*"):
            self.api.get_states(bbox=(0, 0))

    def test_get_states_bbox_err_lat(self):
        with self.assertRaisesRegexp(ValueError, "Invalid reference_latitude 95.8389.*"):
            self.api.get_states(bbox=(95.8389, 47.8229, 5.9962, 10.5226))
        with self.assertRaisesRegexp(ValueError, "Invalid reference_latitude -147.8229.*"):
            self.api.get_states(bbox=(45.8389, -147.8229, 5.9962, 10.5226))

    def test_get_states_bbox_err_lon(self):
        with self.assertRaisesRegexp(ValueError, "Invalid reference_longitude -255.9962.*"):
            self.api.get_states(bbox=(45.8389, 47.8229, -255.9962, 10.5226))
        with self.assertRaisesRegexp(ValueError, "Invalid reference_longitude 210.5226.*"):
            self.api.get_states(bbox=(45.8389, 47.8229, 5.9962, 210.5226))

    def test_state_vector_parsing(self):
        s = StateVector(
            ["cabeef", "ABCDEFG", "USA", 1001, 1000, 1.0, 2.0, 3.0, False, 4.0, 5.0, 6.0, None, 6743.7, "6714", False,
             0])
        self.assertEqual("cabeef", s.icao24)
        self.assertEqual("ABCDEFG", s.callsign)
        self.assertEqual("USA", s.origin_country)
        self.assertEqual(1001, s.time_position)
        self.assertEqual(1000, s.last_contact)
        self.assertEqual(1.0, s.longitude)
        self.assertEqual(2.0, s.latitude)
        self.assertEqual(3.0, s.baro_altitude)
        self.assertEqual(4.0, s.velocity)
        self.assertEqual(5.0, s.heading)
        self.assertEqual(6.0, s.vertical_rate)
        self.assertFalse(s.on_ground)
        self.assertEqual(None, s.sensors)
        self.assertEqual(6743.7, s.geo_altitude)
        self.assertEqual("6714", s.squawk)
        self.assertFalse(s.spi)
        self.assertEqual(0, s.position_source)

    def test_get_my_states_no_auth(self):
        a = OpenSkyApi()
        with self.assertRaisesRegexp(Exception, "No username and password provided for get_my_states!"):
            a.get_my_states()

    @skipIf(len(TEST_USERNAME) < 1, "Missing credentials")
    def test_get_my_states(self):
        r = self.api.get_my_states()
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")

    @skipIf(len(TEST_USERNAME) < 1, "Missing credentials")
    def test_get_my_states_time(self):
        r = self.api.get_my_states(time_secs=int(time.time()) - 10)
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")

    @skipIf(len(TEST_USERNAME) < 1, "Missing credentials")
    def test_get_my_states_datetime(self):
        r = self.api.get_my_states(time_secs=datetime.now())
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")

    @skipIf(len(TEST_USERNAME) < 1, "Missing credentials")
    def test_get_my_states_time(self):
        r = self.api.get_my_states(serials=TEST_SERIAL)
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")

    @skipIf(len(TEST_USERNAME) < 1, "Missing credentials")
    def test_get_my_states_rate_limit(self):
        r = self.api.get_my_states()
        self.assertGreater(len(r.states), 0, "Retrieve at least one State Vector")
        r = self.api.get_my_states()
        self.assertIsNone(r, "Rate limit produces 'None' result")


if __name__ == '__main__':
    unittest.main()
