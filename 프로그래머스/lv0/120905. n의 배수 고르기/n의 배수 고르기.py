def solution(n, numlist):
    answer = [i for i in numlist if not i%n]
    return answer