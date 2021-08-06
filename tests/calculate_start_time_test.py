import sys
import os
from datetime import datetime, timedelta
from ..src.backend import calculate_start_time, ServeSandwich


##Test calculate_state_time
def test_calculate_start_time_empty():
    ##if
    empty_times = []
    ##when
    start_time = calculate_start_time(empty_times)
    ##then
    assert  type(start_time) == datetime

def test_calculate_start_time_fill():
    ##if
    now = datetime.now()
    not_empty_times = [ServeSandwich(now,'john')]
    ##when 
    start_time = calculate_start_time(not_empty_times)
    ##then
    assert start_time == now + timedelta(minutes = 1)


