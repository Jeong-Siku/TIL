def solution(bin1, bin2):
    # 이진수의 합
    # 몫과 나머지를 바탕으로
    # 정수형에서 문자형으로 변경 필요
    # 이진수는 각 자리를 별도로 계산 필요
    bins = int(bin1,2)+int(bin2,2)
    answer = bin(bins)
    return answer[2:]
# 1001 1111 
# 2112
# 21 1 0 10