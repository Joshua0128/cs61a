# Currying - Transforming a multi-argument function into a single-argument, high-order function.

from operator import add, mul
def make_adder(n):
    return lambda k: n+k

def curry2(f):
    def g(x):
        def h(y):
            return f(x, y)
        return h
    return g

curry2 = lambda f: lambda x: lambda y: f(x, y)
# m = curry2(add)

# Decorators
from ucb import trace

def trace1(fn):
    """ Returns a version of fn that first print before it is called.
        
        fn - a function of 1 argument.
    """
    def traced(x):
        print('Calling', fn, 'on argument', x)
        return fn(x)
    return traced



'''
    @trace1
    def square(x):
        return x * x

    the same as:
    
    square = trace1(square)
    
    Decorator is a good way to hide high order function
'''

@trace1
def sum_square_up_to(n):
    k = 1
    total = 0
    while k <= n:
        total, k = total + square(k), k + 1
    return total

# Why python print(print(5))

def delay(arg):
    print('delayed')
    def g():
        return arg
    return g

def pirate(arggg):
    print('matey')
    def plunder(arggg):
        return arggg
    return plunder

def horse(mask):
    horse = mask
    def mask(horse):
        return horse
    return horse(mask)
mask = lambda horse: horse(2)

# implement

def remove(n, digit):
    """ Return all digits of non-negative N
        that are not DIGIT, for some non-negative DIGIT less than 10.
    """
    kept, digits = 0, 0
    while n > 0:
        n, last = n // 10, n % 10
        if last != digit:
            kept = last * (10 ** digits ) + kept
            digits += 1
    return kept

