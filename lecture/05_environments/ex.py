def apply_twice(f, x):
    return f(f(x))

def repeat(f, x):
    while f(x) != x:
        x = f(x)
    return x

def g(y):
    return (y+5) // 3

def square(x):
    return x * x

def make_adder(n):
    def adder(k):
        return k+n
    return adder

def f(x, y):
    def g(a):
        return a+y
    return g(x)

def square(x):
    return x * x

def triple(x):
    return 3 * x

def compose1(f, g):
    def h(x):
        return f(g(x))
    return h

# <func name> = lambda <formal parameter> : <single calc expression>
# only for simple function
squ = lambda x: x * x
print(squ)
print(squ(3))


