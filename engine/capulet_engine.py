from engine.engine import Engine


class CapuletEngine(Engine):
    __SERVICE_MILES_INTERVAL = 30000

    def __init__(self, last_service_mileage: int, current_mileage: int):
        self.__last_service_mileage = last_service_mileage
        self.__current_mileage = current_mileage

    def needs_service(self) -> bool:
        return self.__current_mileage - self.__last_service_mileage >= CapuletEngine.__SERVICE_MILES_INTERVAL
