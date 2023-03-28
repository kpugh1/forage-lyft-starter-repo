from abc import ABC, abstractmethod
from servicable import Servicable

class Tire(Servicable):
    def __init__(self):
        pass
    def needs_service(self):
        return self.needs_service()
    
class CarriganTire(Tire):
    def __init__(self, tireArr):
        super().__init__()
        self.tireArr = tireArr
    
    # Needs service when 1 or more elements is >= 0.9
    def needs_service(self):
        for x in self.tireArr:
            if x >= 0.9:
                return True
        return False

class OctoprimeTire(Tire):
    def __init__(self, tireArr):
        super().__init__()
        self.tireArr = tireArr
        
    # Needs service when the sum of the array is >= 3
    def needs_service(self):
        total = 0
        for x in self.tireArr:
            total += x
            if total >= 3:
                return True
        return total >= 3