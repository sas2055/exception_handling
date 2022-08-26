"""
# Exception:
    - Exception means error.
    - Exceptions are raised when the program is syntactically correct,
    but the code resulted in an error.
    - This error does not stop the execution of the program,
    however, it changes the normal flow of the program.
    - Exception is the base class for all the exceptions in Python.
---------------------------------------------------------------
Example:
    NameError
    TypeError
    ValueError
=====================================================================

# Que. Why to handle exception???

print(100)
print(list(range(5)))
print(a)
print('Hello gm')
print(234234255)
----- if we look at above scenario
because of a next 2 lines won't be executed
so in order to avoid this problem we need Exception handling
=======================================================================

# Que. How to handle exception:
    We have 4 blocks to deal with this
try:
    test the code here
except:
    if exception occurs in try then handle it here in except
else:
   if exception does not occur in try then else
finally:
    it do-not care about exception occur or not this block will be
    an executed always irrespective of exception
==========================================================================

try: # we put a code to test an error
    print(a)

except: # come here if error occurs
    print('Error present')
print('Hello I am ready to execute')
========================================================================

# Que. How to deal with  exception

try:
    print(a)
except:
    print('please assign value to a')
    a = 100
    print(a)
else: # this is optional
    print('No exception')
    for i in range(a):
        print(i)
finally:
    print('Zukega nahi sala')
------------------------------------------------------------------------------

a = 5
try:
    print(a)
except:
    print('please assign value to a')
    a = 100
    print(a)
else: # this is optional
    print('No exception')
    for i in range(a):
        print(i)
finally:
    print('Zukega nahi sala')
===========================================================================

# Que. How to handle typical exception?
- means we know which exception is gonna happen/ occur
-------------------------------------------------------------------

try:
    # print(10/0)
    # print(a)
    # print('1'/3)
    print([].index(10))

except ZeroDivisionError as msg:
    print('Error: ', msg)

except NameError as msg:
    print('Error: ', msg)
    print('Write further logic here')

except TypeError as msg:
    print('Error: ', msg)

# default exception
except:
    print('Default exception')
    try:
        print(e)
    except:
        print('Handled')
======================================================================

# From where u will get names of all exceptions
print(help('builtins'))
print(help(Exception)) # it use hierarchy of exception
======================================================================

# Lets combine multiple exceptions together

try:
    # print(10/0)
    # print(a)
    # print('1'/3)
    # print([].index(10))

except (ZeroDivisionError, NameError) as msg:
    print('Error: ', msg)
======================================================================

# To handle all exceptions under one roof use Exception as a main class

try:
    # print(10/0)
    # print(a)
    # print('1'/3)
    print([].index(10))

except Exception as msg:
    print('Error: ', msg)
======================================================================

- try and except must be there
- use of any one of them is not allowed
------------------------------------------------------------------------

try:    # mandatory
    pass

except: # mandatory
    pass
    try:
        pass
    except:
        pass

else:   # optional
    pass

finally: # optional
    pass
======================================================================

"""