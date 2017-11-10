def fib(n):
   # assert n < 0, "should not be negative"

    if n ==1 :
        return 1
    else:
        return fib(n-1) + fib(n-2)

print (fib(5))
print("**")

print("**")
print(fib(1))