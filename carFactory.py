from datetime import datetime
from car import Car
from battery import nubbin_battery, spindler_battery
from engine import capulet_engine, sternman_engine, willoughby_engine


class CarFactory:
    @staticmethod
    def create_calliope(
            current_date: datetime,
            last_service_date: datetime,
            current_mileage: int,
            last_service_mileage: int
    ) -> Car:
        engine_type = capulet_engine.CapuletEngine(last_service_mileage, current_mileage)
        battery_type = spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine_type, battery_type)

    @staticmethod
    def create_glissade(
            current_date: datetime,
            last_service_date: datetime,
            current_mileage: int,
            last_service_mileage: int
    ) -> Car:
        engine_type = willoughby_engine.WilloughbyEngine(last_service_mileage, current_mileage)
        battery_type = spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine_type, battery_type)

    @staticmethod
    def create_palindrome(
            current_date: datetime,
            last_service_date: datetime,
            warning_light_on: bool
    ) -> Car:
        engine_type = sternman_engine.SternmanEngine(warning_light_on)
        battery_type = spindler_battery.SpindlerBattery(last_service_date, current_date)
        return Car(engine_type, battery_type)

    @staticmethod
    def create_rorschach(
            current_date: datetime,
            last_service_date: datetime,
            current_mileage: int,
            last_service_mileage: int
    ) -> Car:
        engine_type = willoughby_engine.WilloughbyEngine(current_mileage, last_service_mileage)
        battery_type = nubbin_battery.NubbinBattery(last_service_date, current_date)
        return Car(engine_type, battery_type)

    @staticmethod
    def create_thovex(
            current_date: datetime,
            last_service_date: datetime,
            current_mileage: int,
            last_service_mileage: int
    ) -> Car:
        engine_type = capulet_engine.CapuletEngine(current_mileage, last_service_mileage)
        battery_type = nubbin_battery.NubbinBattery(last_service_date, current_date)
        return Car(engine_type, battery_type)
