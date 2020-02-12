'''
It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
'''
import collections
def isMatchingDigits(n,m):
    result = False
    if collections.Counter(list(str(n))) == collections.Counter(list(str(m))):
        result = True
    return result


def GeneratingNumber(n):
    #n digit number
    return 10**n

def PermutedMultiples(n):
    # till n multiple
    i = 1
    result = False
    while not result:
        start_range = GeneratingNumber(i)
        end_range = GeneratingNumber(i+1)
        for j in range(start_range, end_range//n ):
            count = 0
            for factor in range(2, n+1):
                if isMatchingDigits(j, factor*j):
                    count += 1
                else:
                    break
            if count == n - 1 :
                break 
        if count == n -1:
            break
        i += 1
    return j

final = PermutedMultiples(6)
#final = GeneratingNumber(5)
#final = isMatchingDigits(10, 20)
print(final)