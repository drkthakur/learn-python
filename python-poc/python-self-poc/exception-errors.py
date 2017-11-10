# x=8
# while x>5:
#     x=x-1
#     print("Dheeru")

###
#print ("Divisible",10/0)

#print("Dheeru",'2'+2)

x=8
while x>7:
    try:
        x=x-1
        y=10/0
        print("Dheeru")
    except ZeroDivisionError as err:
        print("Why are you dividing it with 0:", err)

try:

    x = int(input("Please enter the number : "))
    if x < 18:
        raise ZeroDivisionError
    x='x'+8
except (ZeroDivisionError, TypeError):
    print('An exception flew by!')

