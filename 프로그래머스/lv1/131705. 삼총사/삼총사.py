def solution(number):
    # 배열
    # 정렬
    # 선택
    # 배열의 길이가 짧다. 그리드 가능
    answer = 0
    for i in range(len(number)-2):
        for j in range(i+1,len(number)-1):
            for k in range(j+1,len(number)):
                if number[i]+number[j]+number[k]==0:
                    answer+=1
    return answer