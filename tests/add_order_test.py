import sys
import os
from datetime import datetime, timedelta
from ..src.backend import add_order, ServeSandwich, MakeSandwich

def test_add_order():
    ##if 
    times = []
    name = 'john'

    ##when
    add_order(name, times)

    ##assert
    now = datetime.now()
    expected = [MakeSandwich(now, name), ServeSandwich(now + timedelta(minutes = 2.5), name)]
    for i in range(len(times)):
        assert times[i].__str__() == expected[i].__str__()