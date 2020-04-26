def square(x):
    return x * x

def sum_squares(x, y):
    return square(x)+square(y)

# Choosing names -> matter a lot for composition
# effect  ex: print()
# behavior  ex: triple()
# value return   ex:abs()

# Which values deserve a name
# from
if sqrt(square(a)+square(b)) > 1:
    x = x + sqrt(square(a)+square(b))

# to
hypotenuse = sqrt(square(a)+square(b))
if hypotenuse > 1:
    x = x + hypotenuse

# Meaningful parts of complex expressions:
# from 
x = (-b + sqrt(square(b)-4*a*c)) / (2*a)

# to
discriminant = sqrt(square(b)-4*a*c)

x = (-b + discriminant) / (2*a)



