from asyncio.windows_events import NULL
import unittest

from factorys.engine_factory import EngineFactory

class TestEngine(unittest.TestCase):
    def test_capulet_engine_not_serviced(self):
        current_mileage = 0
        last_service_mileage = 0
        engine = EngineFactory.create_capulet(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())

    def test_sternman_engine_not_serviced(self):
        warning_light_is_on = False
        engine = EngineFactory.create_sternman(warning_light_is_on)
        self.assertFalse(engine.needs_service())

    def test_willoughby_engine_not_serviced(self):
        current_mileage = 0
        last_service_mileage = 0
        engine = EngineFactory.create_willoughby(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())
    
    def test_capulet_engine_is_serviced(self):
        current_mileage = 90001
        last_service_mileage = 0
        engine = EngineFactory.create_capulet(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_sternman_engine_is_serviced(self):
        warning_light_is_on = True
        engine = EngineFactory.create_sternman(warning_light_is_on)
        self.assertTrue(engine.needs_service())

    def test_willoughby_engine_is_serviced(self):
        current_mileage = 90001
        last_service_mileage = 0
        engine = EngineFactory.create_willoughby(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())