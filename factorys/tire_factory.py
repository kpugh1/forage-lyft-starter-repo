from models.tire import CarriganTire, OctoprimeTire

class TireFactory:
    def create_carrigan(tireArr):
        return CarriganTire(tireArr)
    def create_octoprime(tireArr):
        return OctoprimeTire(tireArr)