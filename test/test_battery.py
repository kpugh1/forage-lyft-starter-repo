from asyncio.windows_events import NULL
import unittest
from datetime import datetime

from factorys.battery_factory import BatteryFactory

class TestBattery(unittest.TestCase):
    def test_nubbin_battery_is_serviced(self):
        last_service_date = datetime.today().replace(year=2018)
        battery = BatteryFactory.create_nubbin(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_splinder_battery_is_serviced(self):
        last_service_date = datetime.today().replace(year=2018)
        battery = BatteryFactory.create_nubbin(last_service_date)
        self.assertTrue(battery.needs_service())

    def test_nubbin_battery_not_serviced(self):
        last_service_date = datetime.today()
        battery = BatteryFactory.create_nubbin(last_service_date)
        self.assertFalse(battery.needs_service())

    def test_splinder_battery_not_serviced(self):
        last_service_date = datetime.today()
        battery = BatteryFactory.create_nubbin(last_service_date)
        self.assertFalse(battery.needs_service())