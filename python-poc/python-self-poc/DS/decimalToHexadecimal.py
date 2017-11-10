import DS.stackImplementation as si


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    s = si.Stack()

    while dec_number > 0:
        rem = dec_number % base
        s.push(rem)
        dec_number = dec_number // base

    new_string = ""

    while not s.is_empty():
        new_string = new_string + digits[s.pop()]

    return new_string


print(base_converter(25, 2))
print(base_converter(25, 8))
print(base_converter(27, 16))