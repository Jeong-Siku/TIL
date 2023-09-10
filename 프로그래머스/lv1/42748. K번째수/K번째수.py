def solution(array, commands):
    # 정렬
    # 인덱스와 a번째 수 차이
    answer = []
    for i,j,k in commands:
        answer.append(sorted(array[i-1:j])[k-1])
        print(array[i-1:j])
    return answer