import timeit
from timeit import Timer

pop_zero = Timer("x.pop(0)", "from __main__ import x")
pop_end = Timer("x.pop()", "from __main__ import x")

x = list(range(200000))
tp_zero = pop_zero.timeit(number = 1000)
print(" time took to pop first Element :", tp_zero)

tp_end = pop_end.timeit(number = 1000)
print(" time took to pop last element:", tp_end)
