""" Tests the outputs of functions in many situations """

from my_module.functions import start, vowels_in_pw, middle, end_points, common

def test_end_points():

    # tests end_points() with a single character and multi-character password
    
    start(True, 'a')

    assert end_points() == ['a']
    
    start(True, 'abc')

    assert end_points() == ['a', 'c']
    
def test_vowels():

    # tests cases for checking upper case vowels and no vowels
    
    start(True, 'aAEgHOIi')

    assert vowels_in_pw() == {'a' : 2, 'e' : 1, 'i' : 2, 'o' : 1, 'u' : 0}
    
def test_middle():
    
    # tests the middle most letter for an odd length password
    
    start(True, 'abc')
    
    assert middle() == 'b'
    
    # tests the two middle most letters for an even length password
    
    start(True, 'abcd')
    
    assert middle() == ['b', 'c']
    
def test_common():
    
    # tests the most common letter, is case sensitive!
    
    start(True, 'bAAaacccb')
    
    assert common() == 'c'
    
    # tests if all letters apear an equal number of times
    
    start(True, 'abcdefg')
    
    assert common() == 'a'
    
    # tests if some letters apear an equal number of times
    
    start(True, 'caabbd')
    
    assert common() == 'a'