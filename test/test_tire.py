import unittest

from factorys.tire_factory import TireFactory

class TestTire(unittest.TestCase):
    def test_carrigan_tire_is_serviced(self):
        tireArr = [0, 1, 0, 0]
        tire = TireFactory.create_carrigan(tireArr)
        self.assertTrue(tire.needs_service())
    def test_octoprime_tire_is_serviced(self):
        tireArr = [1, 1, 1, 1]
        tire = TireFactory.create_octoprime(tireArr)
        self.assertTrue(tire.needs_service())
    def test_carrigan_tire_not_serviced(self):
        tireArr = [0, 0, 0, 0]
        tire = TireFactory.create_carrigan(tireArr)
        self.assertFalse(tire.needs_service())
    def test_octoprime_tire_not_serviced(self):
        tireArr = [0.5, .1, .1, .1]
        tire = TireFactory.create_octoprime(tireArr)
        self.assertFalse(tire.needs_service())