from datetime import datetime
from battery.battery import Battery


class NubbinBattery(Battery):
    __SERVICE_INTERVAL = 4

    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.__last_service_date = last_service_date
        self.__current_date = current_date

    def needs_service(self):
        return (self.__current_date.year - self.__last_service_date.year) >= NubbinBattery.__SERVICE_INTERVAL
