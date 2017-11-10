import DS.stackImplementation as si


def matches(open, close):
    opens = "([{"
    closes = ")]}"
    return opens.index(open) == closes.index(close)


def multiple_par_checker(symbol_string):
    s = si.Stack()
    balanced = True
    index = 0

    while index < len(symbol_string) and balanced:
        symbol = symbol_string[index]
        if symbol in "([{":
            s.push(symbol)
        else:
            if s.is_empty():
                balanced = False
            else:
                top = s.pop()
                if not matches(top, symbol):
                    balanced = False

        index = index + 1

    if balanced and s.is_empty():
        return True
    else:
        return False


print(multiple_par_checker("{}(())[]"))
print(multiple_par_checker("({[(){}]})"))
print(multiple_par_checker("({[(){(}])})"))