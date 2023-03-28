from abc import ABC, abstractmethod
from servicable import Servicable
from models.battery import Battery
from models.engine import Engine
from models.tire import Tire

class Car(Servicable):
    def __init__(self, engine, battery, tire):
        self.engine = engine
        self.battery = battery
        self.tire = tire

    # Needs service when any of the car parts need service
    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service() or self.tire.needs_service()
