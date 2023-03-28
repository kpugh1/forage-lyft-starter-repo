from models.engine import CapuletEngine, SternmanEngine, WilloughbyEngine


class EngineFactory:
    def create_capulet(current_mileage, last_service_mileage):
        return CapuletEngine(current_mileage, last_service_mileage)
    def create_sternman(warning_light_is_on):
        return SternmanEngine(warning_light_is_on)
    def create_willoughby(current_mileage, last_service_mileage):
        return WilloughbyEngine(current_mileage, last_service_mileage)