def minimum_in_list(x):  # minimum_in_list is with linear complexity
    temp = x[0]
    for i in range(len(x)):
        if x[i] < temp:
            temp = x[i]
    return temp


print("%d is smaller values" % minimum_in_list([5,3,6,2]))


def minimum_in_list_1(x):  # minimum_in_list_1 is with n^2 complexity
    small = x[0]
    for i in range(len(x)):
        for j in range(len(x)):
            if x[j] < x[i]:
                small = x[j]
    return small


print("%d is smaller values" % minimum_in_list_1([5,0,6,2]))