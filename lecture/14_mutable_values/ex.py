from datetime import date

today = date(2015, 2, 20)
freedom = date(2015, 5, 12)

today.strftime('%A %B %d')

s = 'Hello'
s = s.upper()

from unicodedata import name, lookup

suits = ['coin', 'string', 'myraid']
original_suits = suits
suits.pop()
suits.remove('string')
suits.append('cup')
suits.extend(['sword', 'club'])
print(suits)

# Identity v.s. Equality
"""Identity
    <exp0> is <exp1>
    evaluates to True if both <exp0> and <exp1> evaluate to the same object.

    Equality
    <exp0> == <exp1>
    evaluates to True if both <exp0> and <exp1> evaluate to equal values

    Identity objects are always equal values
"""
a = [10]
b = [10]
print(a == b)
print(a is b)

c = b
print(c == b)
print(c is b)

def f(s=[]):
    s.append(5)
    return len(s)
