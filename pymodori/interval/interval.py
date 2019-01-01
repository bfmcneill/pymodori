"""This module builds an interval object that can be used in code that requires timers such as pomodor timers"""

from datetime import datetime, timedelta


def datetime_round(dt=None):
    """helper function that truncates a date time object to the nearest second"""
    if not dt:
        dt = datetime.now()

    if dt.microsecond >= 500000:
        dt = dt + timedelta(seconds=1)

    dt = dt.replace(microsecond=0)

    return dt


"""This dictionary helps make the interval status code friendly for humans"""
interval_states = {"ACTIVE": 1, "COMPLETE": 2, "INITIAL": 3}


class Interval:
    """Interval object holds details about the start and stop times of an event"""

    def __init__(self):
        self.status = interval_states["INITIAL"]
        self.datetime_open = None
        self.datetime_close = None

    def open(self):
        """open the interval"""

        if self.status in [interval_states["ACTIVE"], interval_states["COMPLETE"]]:
            raise ValueError("Interval has already been opened")

        self.datetime_open = datetime_round()
        self.status = interval_states["ACTIVE"]
        
    def close(self):
        """close the interval"""
        if self.status in [interval_states["COMPLETE"], interval_states["INITIAL"]]:
            raise ValueError("Interval must be opened before it is closed")

        self.datetime_close = datetime_round()

        if self.datetime_close == self.datetime_open:
            self.datetime_close += timedelta(seconds=1)

        self.status = interval_states["COMPLETE"]

    def duration_calc(self):
        """determine the interval duration in seconds"""
        if self.status in [interval_states["INITIAL"], interval_states["ACTIVE"]]:
            raise ValueError("Interval does not have duration")

        delta = self.datetime_close - self.datetime_open
        return delta.total_seconds()
