'''
Write a function:

def solution(A)

that, given an array A of N integers, returns the smallest positive integer (greater than 0) that does not occur in A.

For example, given A = [1, 3, 6, 4, 1, 2], the function should return 5.

Given A = [1, 2, 3], the function should return 4.

Given A = [−1, −3], the function should return 1.

'''

def solution(A):
    # write your code in Python 3.6
    
    if max(A) < 0:
        return 1
    flag = True
    for i in range(1,len(A)+1):
        if i not in A:
            flag = False
            break
    if flag:
        return(len(A)+1)
    else:
        return(i)

    
A = [1, 3, 6, 4, 1, 2]
print(solution(A))
input()
