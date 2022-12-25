from unittest import TestCase
from engine.willoughby_engine import WilloughbyEngine
from engine.sternman_engine import SternmanEngine
from engine.capulet_engine import CapuletEngine


class TestWilloughbyEngine(TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_engine_with_no_mileage_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(TestCase):
    def test_engine_should_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=True)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        engine = SternmanEngine(warning_light_is_on=False)
        self.assertFalse(engine.needs_service())


class TestCapuletEngine(TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertTrue(engine.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 10000
        last_service_mileage = 0
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())

    def test_engine_with_no_mileage_should_not_be_serviced(self):
        current_mileage = 0
        last_service_mileage = 0
        engine = CapuletEngine(last_service_mileage, current_mileage)
        self.assertFalse(engine.needs_service())
