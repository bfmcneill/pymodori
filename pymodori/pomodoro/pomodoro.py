from datetime import datetime, timedelta


class Pomodoro():
    def __init__(self, minutes=20, seconds=0):
        self.seconds_remaining = minutes*60 + seconds
        self._is_counting = False

    def start(self):
        self._is_counting = True

    def stop(self):
        self._is_counting = False
