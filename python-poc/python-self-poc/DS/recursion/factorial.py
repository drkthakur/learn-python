def factorial(n):
    assert n >= 0
    if n < 2:
        return 1
    else:
        return n * factorial(n -1)



print (factorial(4))