"""Data abstraction: A methodology by which functions enforce
an abstraciton barrier between representation and use
"""

pair = [1, 2]

# Rational arithemetic
def add_rational(x, y):
    """Add rational numbers x and y."""
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    
    return rational(nx * dy + ny * dx, dx * dy)

def mul_rational(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)
    
    return rational(nx * ny, dx * dy)

def rationals_are_equal(x, y):
    nx, dx = numer(x), denom(x)
    ny, dy = numer(y), denom(y)

    return (nx * dy == ny * dx)

def print_rational(x):
    print(f"{numer(x)} / {denom(x)}")

# Constructor and selectors
from fractions import gcd

def rational(n, d):
    """Construct a rational number that represents N/D."""
    g= gcd(n, d)
    return [n//g, d//g]

def numer(x):
    return x[0]

def denom(x):
    return x[1]

def rational(n, d):
    def select(name):
        if name == 'n':
            return n
        elif name == 'd':
            return d
    return select

def numer(x):
    return x('n')

def denom(x):
    return x('d')


