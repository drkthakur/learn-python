def sum_of_n(n):
    the_sum=0
    for i in range(1,n+1):
        the_sum=the_sum+i

    return the_sum


#print(sum_of_n(10))

def foo(tom):
    fred=0
    for bill in range(1, tom+1):
        barney = bill
        fred = fred + barney

    return fred


#print(foo(10))

import time


def sum_of_n_2(n):
    start = time.time()
    the_sum = 0
    for i in range(1, n+1):
        the_sum = the_sum + i
    end = time.time()
    return the_sum, end - start


def sum_of_n_3(n):
    start = time.time()
    the_sum = (n*(n+1))/2
    end = time.time()
    return the_sum, end - start


for i in range(5):
    print("Sum is %d required %10.7f seconds"  % sum_of_n_2(1000000),
          "Maths Power: Sum is %d required %10.7f seconds" % sum_of_n_3(1000000))
