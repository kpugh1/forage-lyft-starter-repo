from abc import ABC, abstractmethod
from servicable import Servicable
from models.battery import Battery
from models.engine import Engine

class Car(Servicable):
    def __init__(self, engine, battery):
        self.engine = engine
        self.battery = battery

    def needs_service(self):
        return self.engine.needs_service() or self.battery.needs_service()
