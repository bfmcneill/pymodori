from unittest.mock import patch
from datetime import datetime
from time import sleep

import pytest

from pymodori.interval.interval import Interval, datetime_round, interval_states


def test_round_down():
    dt = datetime(2018, 12, 30, 4, 5, 6, 480000)
    expected = datetime_round(dt)
    assert expected == datetime(2018, 12, 30, 4, 5, 6)


def test_round_up():
    dt = datetime(2018, 12, 30, 4, 5, 6, 580000)
    expected = datetime_round(dt)
    assert expected == datetime(2018, 12, 30, 4, 5, 7)


@pytest.fixture()
def interval():
    return Interval()


def test_interval_status_is_initial(interval):
    assert interval.status == interval_states["INITIAL"]


def test_interval_status_is_active(interval):
    interval.open()
    assert interval.status == interval_states["ACTIVE"]


def test_interval_status_is_complete(interval):
    interval.open()
    interval.close()
    assert interval.status == interval_states["COMPLETE"]


def test_interval_begin_while_in_process(interval):
    interval.open()
    with pytest.raises(ValueError):
        interval.open()


def test_interval_close_before_open(interval):
    with pytest.raises(ValueError):
        interval.close()


def test_interval_begin_a_completed_process(interval):
    interval.open()
    interval.close()
    with pytest.raises(ValueError):
        interval.open()


def test_interval_duration_calc_mid_process(interval):
    interval.open()
    with pytest.raises(ValueError):
        interval.duration_calc()


def test_interval_duration_calc(interval):
    interval.open()
    sleep(.1)
    interval.close()
    assert interval.duration_calc() == 1
