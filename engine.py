from abc import ABC, abstractmethod
from servicable import Servicable

class Engine(Servicable):
    def __init__(self):
        pass

    def needs_service(self):
        return self.needs_service()

class CapuletEngine(Engine):
    def __init__(self, last_service_date, current_mileage, last_service_mileage):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 30000

class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on):
        super().__init__()
        self.warning_light_is_on = warning_light_is_on

    def needs_service(self):
        if self.warning_light_is_on:
            return True
        else:
            return False

class WilloughbyEngine(Engine):
    def __init__(self,current_mileage, last_service_mileage):
        super().__init__()
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage

    def needs_service(self):
        return self.current_mileage - self.last_service_mileage > 60000

