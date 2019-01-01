from datetime import datetime
from unittest.mock import patch
from pymodori.pomodoro.pomodoro import Pomodoro


def test_create_timer_with_default_time():
    timer = Pomodoro()
    assert timer.seconds_remaining == 60*20


def test_create_timer_with_specified_amount_of_time():
    timer = Pomodoro(minutes=19, seconds=59)
    assert timer.seconds_remaining == 60*19+59


def test_state_timer_default():
    timer = Pomodoro()
    expected = False
    assert expected == timer._is_counting


def test_state_timer_start():
    timer = Pomodoro()
    timer.start()
    expected = True
    assert expected == timer._is_counting


def test_state_timer_stop():
    timer = Pomodoro()
    timer.stop()
    expected = False
    assert expected == timer._is_counting


def test_time_remaining():
    timer = Pomodoro(minutes=19, seconds=59)
    expected = 60*19+59
    assert expected == timer.seconds_remaining
