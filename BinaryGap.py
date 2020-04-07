#BinaryGap
#Find longest sequence of zeros in binary representation of an integer.
'''
given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001
and so its longest binary gap is of length 5.
Given N = 32 the function should return 0, because N has binary representation '100000' and thus no binary gaps.
''''

def binaryGap(N):
    N = bin(N).replace("0b", "")

    if N.count("0") == 0 or N.count("1") < 2:
        return 0

    count_list = []
    count = 0
    for i in range(1,len(N)):
        if N[i] == "0":
            count += 1
        elif N[i] == "1":
            count_list.append(count)
            count = 0

    return max(count_list)

N = int(input("Enter N : "))
print("Longest sequence of zero in binary representation is : ",binaryGap(N))
input()
