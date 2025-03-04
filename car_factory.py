
from engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from battery import NubbinBattery, SplindlerBattery
from car import Car

class CarFactory():
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)

    def create_glissade(current_date, last_service_date, current_mileage, last_service_mileage):
        engine =  WilloughbyEngine(current_mileage, last_service_mileage)
        battery =  SplindlerBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)

    def create_palindrome(current_date, last_service_date, warning_light_on):
        engine = SternmanEngine(warning_light_on)
        battery = SplindlerBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)

    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)

    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage):
        engine = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        return Car(engine=engine, battery=battery)

