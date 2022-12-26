from tyre.tyre import Tyre


class OctoprimeTyre(Tyre):
    TYRE_WEAR_THRESHOLD = 3

    def __init__(self, tyre_wear_reading):
        self.__tyre_wear_reading = tyre_wear_reading

    def needs_service(self):
        return sum(self.__tyre_wear_reading) >= self.TYRE_WEAR_THRESHOLD
