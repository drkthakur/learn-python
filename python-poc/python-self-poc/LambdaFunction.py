def make_incrementor(n):
    return lambda x: x + n

f=make_incrementor(10)
print(f(1))

[a,b]=[1,2]
print("a:",1,"b:",b)