from serviceable import Serviceable
from battery.battery import Battery
from engine.engine import Engine
from tyre.tyre import Tyre


class Car(Serviceable):
    def __init__(self, engine: Engine, battery: Battery, tyre: Tyre):
        self.__engine = engine
        self.__battery = battery
        self.__tyre = tyre

    def needs_service(self):
        return self.__engine.needs_service() or \
            self.__battery.needs_service() or \
            self.__tyre.needs_service()
