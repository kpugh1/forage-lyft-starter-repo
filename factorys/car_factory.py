from engine_factory import EngineFactory
from battery_factory import BatteryFactory
from tire_factory import TireFactory

from models.car import Car

class CarFactory:
    def create_calliope(current_mileage, last_service_mileage, last_service_date, tireArr):
        engine = EngineFactory.create_capulet( current_mileage, last_service_mileage)
        battery = BatteryFactory.create_splinder(last_service_date)
        tire = TireFactory.create_carrigan(tireArr)
        return Car(engine=engine, battery=battery, tire=tire)

    def create_glissade(current_mileage, last_service_mileage, last_service_date, tireArr):
        engine =  EngineFactory.create_willoughby(current_mileage, last_service_mileage)
        battery =  BatteryFactory.create_splinder(last_service_date)
        tire = TireFactory.create_octoprime(tireArr)
        return Car(engine=engine, battery=battery, tire=tire)

    def create_palindrome( warning_light_on, last_service_date, tireArr):
        engine = EngineFactory.create_sternman(warning_light_on)
        battery = BatteryFactory.create_splinder(last_service_date)
        tire = TireFactory.create_carrigan(tireArr)
        return Car(engine=engine, battery=battery, tire=tire)

    def create_rorschach(current_mileage, last_service_mileage, last_service_date, tireArr):
        engine = EngineFactory.create_willoughby(current_mileage, last_service_mileage)
        battery = BatteryFactory.create_nubbin(last_service_date)
        tire = TireFactory.create_octoprime(tireArr)
        return Car(engine=engine, battery=battery, tire=tire)

    def create_thovex(current_mileage, last_service_mileage, last_service_date, tireArr):
        engine = EngineFactory.create_capulet(current_mileage, last_service_mileage)
        battery = BatteryFactory.create_nubbin(last_service_date)
        tire = TireFactory.create_carrigan(tireArr)
        return Car(engine=engine, battery=battery, tire=tire)

