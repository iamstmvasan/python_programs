#CyclicRotation
#Rotate an array to the right by a given number of steps.

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
