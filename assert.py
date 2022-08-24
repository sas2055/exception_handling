"""
# Assert keyword:
    - it is used when debugging code and testing.
    - if a condition is True then output there clear execution of
    a code and program to continue to run.
    - if a condition is False then program will raise an AssertionError and stop.
    - Python has built-in assert statement to use assertion condition in the program.
----------------------------------------------------------------------
syntax:
    assert <condition>
---------------------------------------------------------------------
assert 4 < 20
print('hello')
=====================================================================

assert <condition>, <error message>
assert 1!=1, 'Your condition results False'
=====================================================================

def test(data):
    assert len(data) != 0, 'List is empty'
    return sum(data), sum(data)/len(data)
print(test([1,2,3]))
print(test([]))
=====================================================================

========================================================
"""
