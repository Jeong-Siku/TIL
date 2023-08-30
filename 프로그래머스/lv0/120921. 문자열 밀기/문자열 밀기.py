def solution(A, B):
    answer = 0
    for _ in range(len(A)):
        if A==B:
            return 0
        if A[-1]+A[:-1] == B:
            answer+=1
            return answer
        else:
            A = A[-1]+A[:-1]
            answer+=1
    return -1