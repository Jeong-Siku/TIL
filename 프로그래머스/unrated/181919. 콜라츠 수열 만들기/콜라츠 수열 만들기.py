# def solution(n):
#     answer = []
#     answer.append(n)
#     while n!=1:
#         if n%2==0:
#             n//=2
#         elif n%2==1:
#             n=n*3+1
#         answer.append(n)
#     return answer

def solution(n):
    answer = []
    answer.append(n)
    while n!=1:
        n = n//2 if n%2==0 else n*3+1
        answer.append(n)
    return answer