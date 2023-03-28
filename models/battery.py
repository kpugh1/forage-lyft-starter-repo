from abc import ABC, abstractmethod
from servicable import Servicable
from datetime import datetime

class Battery(Servicable):
    def __init__(self):
        pass

    def needs_service(self):
        return self.needs_service()

class NubbinBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__()
        self.last_service_date = last_service_date

    #Needs service every 4 years from last service date
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 4)
        if service_threshold_date < datetime.today():
            return True
        else:
            return False

class SplindlerBattery(Battery):
    def __init__(self, last_service_date):
        super().__init__()
        self.last_service_date = last_service_date

    #Needs service every 3 years from last service date
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        if service_threshold_date < datetime.today():
            return True
        else:
            return False
