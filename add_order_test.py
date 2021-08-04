import backend

def test_add_order():
    ##if 
    times = []
    name = 'john'

    ##when
    backend.add_order(name, times)

    ##assert
    expected = [backend.MakeSandwich(0, name), backend.ServeSandwich(2.5, name)]
    for i in range(len(times)):
        assert times[i].__str__() == expected[i].__str__()