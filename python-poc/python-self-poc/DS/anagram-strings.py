#Solution1: Checking off iteration
#Our  first  solution  to  the  anagram  problem  will  check  to  see  that  each  character  in  the  first
#string actually occurs in the second.   If it is possible to “checkoff” each character,  then the
#two strings must be anagrams

def anagram_solution_1(s1, s2):
    a_list = list(s2)
    pos1 = 0
    still_ok = True

    while pos1 < len(s1) and still_ok:
        pos2 = 0
        found = False

        while pos2 < len(s1) and not found:
            if s1[pos1] == a_list[pos2]:
                found = True
            else:
                pos2 = pos2 +1

        if found:
            a_list[pos2] = None
        else:
            still_ok = False

        pos1 = pos1 + 1

    return still_ok


print(anagram_solution_1("Dheeru", "rueehD"))
print(anagram_solution_1("Dheeru", "Monkey"))


#Solution2: Sorting and compare

# Below solution seems to be of order(n) but the sorting is not without there own cost.
# So sorting comes with either O(n^2) or O(nlogn)
# So sorting dominates the iteration
# Below solution comes with O(n) to search and O(nlogn) to sort thus results into O(nlogns)

def anagram_solution_2(s1, s2):
    a_list1 = list(s1)
    a_list2 = list(s2)

    a_list1.sort()
    a_list2.sort()

    pos = 0
    matches = True

    while pos < len(s1) and matches:
        if a_list1[pos] == a_list2[pos]:
            pos = pos +1
        else:
            matches = False
    return matches

print(anagram_solution_2("Dheeru", "rueehD"))
print(anagram_solution_2("Dheeru", "Monkey"))

# Solution3: Brute Force

## Brute force technique for anagram solution
# typically tries to exhaust all the possibilities
#For the anagram detection problem, we can simply generate a list of all possible strings using the characters from s1 and then see if s2 occurs.
# When generating all possible strings from s1 there are n possible characters n-1 possible character for second position, n-2 for third and so on.
# total number of candidate string is n * n-1 * n-2 * n-3 ---- 2 1
# which results to factorial n.

#Solution 4:  Count and compare

#the fact that any two anagrams will have the same number of a’s, the same number of b’s, the same number of c’s, and so on.
#In order to decide whether two strings are anagrams, we will first count the number of times
#each character occurs. Since there are 26 possible characters, we can use a list of 26 counters,
#one for each possible character. Each time we see a particular character, we will increment the
#counter at that position. In the end, if the two lists of counters are identical, the strings must be anagrams


#In other words, this algorithm sacrificed space in order to gain time.


#This is a common occurrence.  On many occasions you will need to make decisions between
#time and space trade-offs.  In this case, the amount of extra space is not significant.  However,
#if  the  underlying  alphabet  had  millions  of  characters,  there  would  be  more  concern.   As  a
#computer scientist, when given a choice of algorithms, it will be up to you to determine the
#best use of computing resources given a particular problem

def anagram_solution_4(s1, s2):
    c1 = [0] * 26
    c2 = [0] * 26

    for i in range(len(s1)):
        pos = ord(s1[i]) - ord('a')
        c1[pos] = c1[pos] + 1

    for i in range(len(s2)):
        pos = ord(s2[i]) - ord('a')
        c2[pos] = c2[pos] +1

    j = 0
    still_ok = True
    while j < 26 and still_ok:
        if c1[j] == c2[j]:
            j = j + 1
        else:
            still_ok = False

    return still_ok


print(anagram_solution_4("Dheeru", "rueehD"))

