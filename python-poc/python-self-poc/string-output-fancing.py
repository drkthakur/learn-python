s="heyy! Hello"

print(str(s))# Human readable
print(repr(s))# Interpreter readble

for x in range(1,11):
    print(repr(x),repr(x*x),repr(x*x*x))