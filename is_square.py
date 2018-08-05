
'''
A square of squares
Task
Given an integral number, determine if it's a square number:

In mathematics, a square number or perfect square is an integer that is the square of an integer; in other words, it is the product of some integer with itself.

The tests will always use some integral number.

Examples:
is_square (-1) # => false
is_square   0 # => true
is_square   3 # => false
is_square   4 # => true
is_square  25 # => true
is_square  26 # => false
'''
import math

def is_square(n):
    if n < 0:
        return False
    return (int(math.sqrt(n)) - math.sqrt(n)) == 0
