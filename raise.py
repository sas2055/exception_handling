"""
# raise keyword:
    - it is used to raise an exceptions or errors.
    - it raises an error and stops the control flow of the program.
    - it is mainly used for exception handling.
    - You can define what kind of error to raise, and the text to print to the user.
-------------------------------------------------------------------------
Syntax:
    raise  {name_of_the_exception_class}
--------------------------------------------------------------------------

# Que. How to generate an exception
->    use raise keyword
    raise is used to customize exceptions
-----------------------------------------------------------------------

# we need to specify condition for which this exception will get raised
# if we want to allow only adults
age = 13
if age <= 18:
    try:
        raise Exception('Error ala re....')
    except:
        print('Error handled')
else:
    print('Welcome to this...')
=========================================================================

x = -1
if x < 0:
    raise Exception('Sorry, no numbers below zero')
=========================================================================

s = 'apple'
try:
    num = int(s)
except ValueError:
    raise ValueError("String can't be changed into integer")
===========================================================================

a = 13
b = 11
try:
    if a < 0 or b < 0:
        raise ZeroDivisionError
    print(a/b)
except ZeroDivisionError:
    print('Please enter valid integer value')
=================================================================

# Personalized exceptions/Customized exceptions:
    - Every exception is one class
    - users can define custom exceptions by creating a new class
    that inherits from the built-in exception class.
-----------------------------------------------------------------

class Shiv(Exception):
    def __init__(self, msg):
        self.msg = msg

amt = float(input('How much money do you have: '))
if amt < 10000:
    raise Shiv('Sir plz bring more money them will think')
else:
    print('Welcome to my Team')
============================================================

# Select employees between age 18 to 50
# if age > 60 then generate old exception
# if age < 18 then generate young exception

class Young(Exception):
    def __init__(self, msg):
        self.msg = msg

class Old(Exception):
    def __init__(self, msg):
        self.msg = msg

age = int(input('Enter the age: '))
if age > 60:
    raise Old('Your age is already crossed.....Sorry')
elif age < 18:
    raise Young('Please wait for sometime....')
else:
    print('You are eligible')
===========================================================
"""
