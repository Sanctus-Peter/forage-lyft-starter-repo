from serviceable import Serviceable
from battery.battery import Battery
from engine.engine import Engine


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery):
        self.__engine = engine
        self.__battery = battery

    def needs_service(self):
        return self.__engine.needs_service() or self.__battery.needs_service()
