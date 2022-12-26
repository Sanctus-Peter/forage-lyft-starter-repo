from tyre.tyre import Tyre


class CarriganTyre(Tyre):
    TYRE_WEAR_THRESHOLD = 0.9

    def __init__(self, tyre_wear_reading):
        self.__tyre_wear_reading = tyre_wear_reading

    def needs_service(self):
        return any(x >= CarriganTyre.TYRE_WEAR_THRESHOLD for x in self.__tyre_wear_reading)
