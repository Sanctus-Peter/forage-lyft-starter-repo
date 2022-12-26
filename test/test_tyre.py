from unittest import TestCase
from tyre.carrigan_tyre import CarriganTyre
from tyre.octoprime_tyre import OctoprimeTyre


class TestCarriganTyre(TestCase):
    def test_tyre_should_be_serviced(self):
        tyre = CarriganTyre([0.9, 0.8, 0.7, 0.6])
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre = CarriganTyre([0.8, 0.7, 0.6, 0.5])
        self.assertFalse(tyre.needs_service())

    def test_tyre_with_no_wear_should_not_be_serviced(self):
        tyre = CarriganTyre([0, 0, 0, 0])
        self.assertFalse(tyre.needs_service())


class TestOctoprimeTyre(TestCase):
    def test_tyre_should_be_serviced(self):
        tyre = OctoprimeTyre([0.9, 0.8, 0.7, 0.6])
        self.assertTrue(tyre.needs_service())

    def test_tyre_should_not_be_serviced(self):
        tyre = OctoprimeTyre([0.8, 0.3, 0.6, 0.1])
        self.assertFalse(tyre.needs_service())

    def test_tyre_with_no_wear_should_not_be_serviced(self):
        tyre = OctoprimeTyre([0, 0, 0, 0])
        self.assertFalse(tyre.needs_service())
