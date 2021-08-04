import backend

def test_generate_string():
    #if
    stuff = ['one', 'two', 'three']

    #when
    string = backend.generate_string(stuff)
    ##then
    expected = '1. one\n2. two\n3. three\n4. Take a break\n'
    assert string == expected