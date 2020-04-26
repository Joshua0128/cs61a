def end(n, d):
    while n > 0:
        last, n = n%10, n // 10
        print(last)
        if d == last:
            return None

def search(f):
    x = 0
    while True:
        if f(x):
            return x
        x += 1

def is_three(x):
    return x == 3

square = lambda x: x*x

def positive(x):
    return max(0, square(x)-100)

def inverse(f):
    """ Return g(y) such that g(f(x)) -> x. """
    return lambda y: search(lambda x: f(x) == y)

def print_all(x):
    print(x)
    return print_all

def print_sums(x):
    print(x)
    def next_sum(y):
        return print_sums(x+y)
    return next_sum

# control 
def if_(c, t, f):
    if c:
        return t
    else:
        return f

from math import sqrt

def real_sqrt(x):
    """ The real part of the square root of X. """
    return if_(x>0, sqrt(x), 0.0)

def has_big_sqrt(x):
    return x > 0 and sqrt(x) > 10

def reasonable(n):
    return n == 0 or 1/n != 0

abs(1/x if x!=0 else 0)
