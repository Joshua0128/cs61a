
odds = [1, 3, 5, 7, 9]
length_of_list = len(odds)

digits = [1, [2,2], 4, 5]
# print(1 in digits)
# print([2,2] in digits)


def count(s, value):
    """Count the number of occurances of value 
    in sequence s.
    """
    total, index = 0, 0
    while index < len(s):
        element = s[index]
        if element == value:
            total += 1
        index += 1
    return total

def count_for(s, value):
    
    total = 0
    for element in s:
        if element == value:
            total += 1
    return total

pairs = [[1,2], [2,2], [3,3], [4,4]]

def same_pair(s):
    sum = 0
    for x, y in pairs:
        if x == y:
            sum += 1
    return sum

"""
    Range : a range is a suquence of consecutive intergers.
    
    range(-2, 2) :: -2, -1, 0, 1
    
    Length: ending value - starting value
    Element selection - starting value + index
"""
# list consturctutor 
range_list = list(range(4))

def sum_below(n):
    total = 0
    for i in range(n):
        total += i
    return total

def cheer():
    for _ in range(3):
        print('Go Bears')

# print([x+1 for x in odds])
# print([x for x in odds if 25 % x == 0])

def divisors(n):
    return [1] + [x for x in range(2, n+1) if n % x == 0]

"""
    Strings are an Abstraction
"""
src = 'curry = lambda f: lambda x: lambda y: f(x, y)'

"""Dictionary : allow us to associate values and keys
"""

numerals = {'I': 1, 'V': 5,'X': 10}

squares = {x:x*x for x in range(10)}

