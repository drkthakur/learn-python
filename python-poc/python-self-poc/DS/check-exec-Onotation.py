a = 5
b = 6
c = 10
    # above is constant 3
for i in range(n):
    for j in range(n):
        x = i*i
        y = j*j
        z = i*j
  # above nested loop is 3n^2 : Because 3 statements performed n^2 times

for k in range(n):
    w = a * k + 45
    v = b * b
 # here is liner range for 2 assignments : 2n

d = 33

# assigments 1 time

# totally complexity of assigments is 3n^2 + 2n + 3 + 1 = 3n^2 + 2n + 4

# As n grows larger n^2 is dominant thus it is O(f(n^2)) = O(n^2)

