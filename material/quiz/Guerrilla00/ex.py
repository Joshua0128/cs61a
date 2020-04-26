
# 4.2

def pow(x, y):
    return  x ** y

foo = lambda x: lambda y: lambda z: x+ y * z

def make_skipper(n):
    """
    >>> a = make_skipper(2)
    >>> a(5)
    1
    3
    5
    """
    def skipper(x):
        for i in range(x+1):
            if i % n != 0:
                print(i)
    return skipper

