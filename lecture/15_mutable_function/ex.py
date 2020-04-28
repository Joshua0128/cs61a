
def percent_difference(x, y):
    difference = abs(x-y)
    return 100 * difference / x
# Bind the names on the left to the resulting values in the current frame!!
diff = percent_difference(40, 50)


def make_withdraw(balance):
    def withdraw(amount):
        nonlocal balance 
        if balance < amount:
            return 'Insufficient funds'
        balance = balance - amount
        return balance
    return withdraw

""" Nonlocal statement 
    Names listed in a nonlocal statement must refer to pre-existing bindings in an enclosing scope.
    Names listed in a nonlocal statement must not collide with pre-existing binding in the local scope(current frame)
"""

# Mutable values can be changed without a nonlocal statement

def make_withdraw_list(balance):
    b = [balance]
    def withdraw(amount):
        if amount > b[0]
            return 'Insufficient funds'
        b[0] = b[0] - amount
        return b[0]
    return withdraw

# Expressions are referentially transparent if substituting an expersion with its value does not change the meaning of a program.
# mutation violate the referentially transparent

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x+1
            return x+y+z
        return h
    return g
a = f(1)
b = a(2)
total = b(3) + b(4)

# if replace b(3) by its value 10

def f(x):
    x = 4
    def g(y):
        def h(z):
            nonlocal x
            x = x+1
            return x+y+z
        return h
    return g
a = f(1)
b = a(2)
total = 10 + b(4)

# total has different result! it's not referentially transparent!
