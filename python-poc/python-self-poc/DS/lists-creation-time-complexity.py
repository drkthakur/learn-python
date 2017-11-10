#Two common operations are indexing and assigning to an index position take the same amount of time no matter how large the list becomes.

#There are two ways to create a longer list.
    #you can use the append method or the concatenation operator. The append method is (1) the concatenation operator is where
    #O(k) is the size of the list that is being concatenated

import timeit
from timeit import Timer
def test1():
    list1 = []
    for i in range(1000):
        list1 = list1 + [i]
def test2():
    list2 = []
    for i in range(1000):
        list2.append(i)
def test3():
    list3 = [i for i in range(1000)]
def test4():
    list4 = list(range(1000))
t1 = Timer("test1()", "from __main__ import test1")
print("concat:", t1.timeit(number = 10000), "milliseconds")

t2 = Timer("test2()", "from __main__ import test2")
print("append:", t2.timeit(number = 10000), "milliseconds")

t3 = Timer("test3()", "from __main__ import test3")
print("Comprehension:", t3.timeit(number = 10000), "milliseconds")

t4 = Timer("test4()", "from __main__ import test4")
print("range:", t4.timeit(number = 10000), "milliseconds")