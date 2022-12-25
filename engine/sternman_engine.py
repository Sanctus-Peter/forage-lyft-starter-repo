from engine.engine import Engine


class SternmanEngine(Engine):
    def __init__(self, warning_light_is_on: bool):
        self.__warning_light_is_on = warning_light_is_on

    def needs_service(self):
        return True if self.__warning_light_is_on else False
