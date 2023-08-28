def solution(my_str, n):
    answer = []
    for i in range(0,len(my_str),n):
        answer.append(my_str[i:i+n])
        # 인덱싱은 범위 에러가 날 수 있지만 슬라이싱은 에러가 나지않음
    return answer