
from models.engine import CapuletEngine, SternmanEngine, WilloughbyEngine
from models.battery import NubbinBattery, SplindlerBattery
from models.car import Car

class CarFactory:
    def create_calliope(current_mileage, last_service_mileage, last_service_date):
        engine = CapuletEngine( current_mileage, last_service_mileage)
        battery = SplindlerBattery(last_service_date)
        return Car(engine=engine, battery=battery)

    def create_glissade(current_mileage, last_service_mileage, last_service_date):
        engine =  WilloughbyEngine(current_mileage, last_service_mileage)
        battery =  SplindlerBattery(last_service_date)
        return Car(engine=engine, battery=battery)

    def create_palindrome( warning_light_on, last_service_date,):
        engine = SternmanEngine(warning_light_on)
        battery = SplindlerBattery(last_service_date)
        return Car(engine=engine, battery=battery)

    def create_rorschach(current_mileage, last_service_mileage, last_service_date):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine=engine, battery=battery)

    def create_thovex(current_mileage, last_service_mileage, last_service_date):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date)
        return Car(engine=engine, battery=battery)

