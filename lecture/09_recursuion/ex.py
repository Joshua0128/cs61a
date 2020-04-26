"""
Definition : A func is callexd recresive iff the body of that func calls iteself, either directly or indirectly.

That is, Executing the body of the recursive func may require applying that func again.
"""

def split(n):
    return n // 10, n % 10

def sum_digits(n):
    """Return the sum of the digits of positive number """
    # base case
    if n < 10:
        return n
    # recursive case
    else:
        all_but_last, last = split(n)
        return sum_digits(all_but_last) + last

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)


"""
Verify it.
1. Verify the base case.
2. Treat fact() as a functional abstraction!
3. Assume that fact(n-1) is correct.
4. Verify that fact(n) is correct, assuming that fact(n-1) is correct.
"""

"""
The Luhn Algorithm.
Used to verify credit card numbers

1. From the rightmost digit, which is the check digit, moving left, double the value of every second digit; if product of this doubling operaiton is greater than 9
(e.g., 7 * 2 = 14), then sum the digits of the products. (e.g., 14 = 1 + 4 = 5)
2. Take the sum of all the digits.
    eg: 138743
       *1 -> 2
        3 -> 3
       *8 -> 7
        7 -> 7
       *4 -> 8
        3 -> 3 check digit

    sum = 30, The Luhn sum of a valid credit card number is a multiple of 10.
"""

def luhn_sum(n):
    if n < 10:
        return n
    else:
        all_but_last, last = split(n)
        return luhn_sum_double(all_but_last) + last

def luhn_sum_double(n):
    all_but_last, last = split(n)
    luhn_digit = sum_digits(2 * last)
    # print(f"{last}, {luhn_digit}")
    if n < 10:
        return luhn_digit
    else:
        return luhn_sum(all_but_last) + luhn_digit

"""
    recursion v.s. iteration
"""

"""
    Converting Recursion to Iteration

    Idea : Figure out what state must be maintained by the iterative function.
"""

def sum_digits_iter(n):
    digit_sum = 0

    while n > 0:
        n, last = split(n)
        digit_sum = digit_sum + last

    return digit_sum

"""
    Converting Iteration to Recursion

    Idea : The state of an iteration can be passed as arguments
"""

def sum_digits_rec(n, digit_sum):
    if n == 0:
        return digit_sum
    else:
        n, last = split(n)
        return sum_digits_rec(n, digit_sum + last)


