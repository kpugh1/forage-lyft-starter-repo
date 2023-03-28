from models.battery import NubbinBattery, SplindlerBattery

class BatteryFactory:
    def create_nubbin(last_service_date):
        return NubbinBattery(last_service_date=last_service_date)
    def create_splinder(last_service_date):
        return SplindlerBattery(last_service_date=last_service_date)