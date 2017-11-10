def pascal(n):
    line = 1
    while(line <= n):
        C = 1
        i = 1
        while(i <= line):
            print(C)
            C = C * (line - i)/i
            i = i + 1
        print("\n")
        line = line + 1



print(pascal(5))
