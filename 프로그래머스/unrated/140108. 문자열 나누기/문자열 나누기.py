# from collections import defaultdict
# def solution(s):
#     answer = 0
#     # 횟수
#     # 같아지는 횟수
#     # 분리
#     # 남은 부분
#     # 반복
#     dic = defaultdict(int)
#     alp=''
    
#     for i in s:
#         if not alp:
#             alp=i
#             dic[alp]=1
#         elif i==alp:
#             dic[alp]+=1
#         else:
#             dic["d"]+=1
#         if dic[alp]==dic["d"]:
#             answer+=1
#             print(dic)
#             dic = defaultdict(int)
#             alp = ""
#     if dic:
#         answer+=1
        
#     return answer

# 프로그래머스 | 문자열 나누기
def solution(s):
    first_alp = "" #첫 글자
    s_count = 0 #첫 글자와 같은 글자 수
    d_count = 0 #첫 글자와 다른 글자 수
    result = 0 #결과값
    for alp in s:

        if first_alp == "":
            first_alp = alp
            s_count = 1
            continue

        if first_alp == alp:
            s_count += 1
        else:
            d_count += 1
        if s_count == d_count:
            first_alp = ""
            s_count = 0
            d_count = 0
            result += 1
    if first_alp != "":
        result += 1
    
    return result