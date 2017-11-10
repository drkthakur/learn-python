smallest = None
largest = None

while True:
    x = input("Enter Number:")
    if x == 'done':
        break
    else:
        try:
            numberIs = int(x)
            if smallest is None:
                smallest = numberIs
                largest = numberIs
            elif numberIs < smallest:
                smallest = numberIs
            elif numberIs > largest:
                largest = numberIs
        except:
            print("Invalid input")

print("Maximum is", largest)
print("Minimum is", smallest)




