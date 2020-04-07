#CyclicRotation
#Rotate an array to the right by a given number of steps.
'''
The goal is to rotate array A K times; that is, each element of A will be shifted to the right K times.
Write a function:
def solution(A, K)
that, given an array A consisting of N integers and an integer K, returns the array A rotated K times.
For example, given
    A = [3, 8, 9, 7, 6]    K = 3
the function should return [9, 7, 6, 3, 8]. Three rotations were made:

    [3, 8, 9, 7, 6] -> [6, 3, 8, 9, 7]
    [6, 3, 8, 9, 7] -> [7, 6, 3, 8, 9]
    [7, 6, 3, 8, 9] -> [9, 7, 6, 3, 8]
For another example, given

    A = [0, 0, 0]
    K = 1
the function should return [0, 0, 0]

Given

    A = [1, 2, 3, 4]
    K = 4
the function should return [1, 2, 3, 4]
'''

def solution(A, K):
    if len(A) == 0:
        return A
    if K >= len(A):
        K = K%len(A)
    for i in range(K):
        for j in range(len(A)-1,0,-1):
            c = A[j]
            A[j] = A[j-1]
            A[j-1] = c
    
    return A

print(solution([1,2,3,4,5], 4))
input()

#output : [2, 3, 4, 5, 1]
