from datetime import datetime
from unittest import TestCase
from battery.spindler_battery import SpindlerBattery
from battery.nubbin_battery import NubbinBattery


class TestNubbinBattery(TestCase):
    def test_battery_should_not_be_serviced(self):
        current_year = datetime.today()
        last_service_year = current_year.replace(year=current_year.year - 2)
        battery = NubbinBattery(last_service_year, current_year)
        self.assertFalse(battery.needs_service())

    def test_battery_should_be_service(self):
        current_year = datetime.today()
        last_service_year = current_year.replace(year=current_year.year - 5)
        battery = NubbinBattery(last_service_year, current_year)
        self.assertTrue(battery.needs_service())

    def test_band_new_battery_should_not_be_serviced(self):
        current_year = datetime.today()
        last_service_year = current_year
        battery = NubbinBattery(last_service_year, current_year)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(TestCase):
    def test_battery_should_not_be_serviced(self):
        current_year = datetime.today()
        last_service_year = current_year.replace(year=current_year.year - 1)
        battery = SpindlerBattery(last_service_year, current_year)
        self.assertFalse(battery.needs_service())

    def test_battery_should_be_service(self):
        current_year = datetime.today()
        last_service_year = current_year.replace(year=current_year.year - 2)
        battery = SpindlerBattery(last_service_year, current_year)
        self.assertTrue(battery.needs_service())

    def test_band_new_battery_should_not_be_serviced(self):
        current_year = datetime.today()
        last_service_year = current_year
        battery = SpindlerBattery(last_service_year, current_year)
        self.assertFalse(battery.needs_service())
