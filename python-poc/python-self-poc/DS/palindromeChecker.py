import DS.dequeueImplementation as di


def pal_checker(a_string):
    char_deq = di.Deque()

    for ch in a_string:
        char_deq.add_rear(ch)

    still_equal = True

    while char_deq.size() > 1 and still_equal:
        first = char_deq.remove_front()
        last = char_deq.remove_rear()
        if first != last:
            still_equal = False

    return still_equal

print(pal_checker('ab'))
