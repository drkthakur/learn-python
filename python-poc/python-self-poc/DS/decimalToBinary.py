import DS.stackImplementation as si


def convert_to_binary(decimal_number):
    s =si.Stack()
    bin_string = ""
    while decimal_number > 0:
        rem = decimal_number % 2
        s.push(rem)
        decimal_number = decimal_number // 2

    while not s.is_empty():
        bin_string = bin_string + str(s.pop())

    return  bin_string


print(convert_to_binary(7))