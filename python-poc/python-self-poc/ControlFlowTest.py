# x = int(input("Please enter the number : "))
x = 20
if x < 0:
    x = 0
    print("Entered value is negative and changed to zero")

elif x == 0:
    print("Zero Value")

elif x == 1:
    print("Value is 1")

else:
    print("print more")

# For loop
print("#############################")
words = ["Dheeru", "Kumar", "Singh"]
for w in words:
    print(w, len(w))

for i in range(5):
    print(i,end=",")

for n in range(2,10):
    for x in range(2,n):
        if n % x == 0:
            print(n, 'equals', x , '*' , n/x)
            break
        else:
            print(n," is a prime number")

for num in range(2,10):
    if num%2==0:
        print("Found an even Number :",num)
        continue
    print("Found an odd Number :", num)

    ###########################################

# def fib(n):
#     a, b = 0, 1
#     while a < n:
#      print(a, end=",")
#     a, b = b, a + b
#
# fib(10)

