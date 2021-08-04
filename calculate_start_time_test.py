import backend


##Test calculate_state_time
def test_calculate_start_time_empty():
    ##if
    empty_times = []
    ##when
    start_time = backend.calculate_start_time(empty_times)
    ##then
    assert  start_time == 0

def test_calculate_start_time_fill():
    ##if
    not_empty_times = [backend.ServeSandwich(10,'john')]
    ##when 
    start_time = backend.calculate_start_time(not_empty_times)
    ##then
    assert start_time == 11
