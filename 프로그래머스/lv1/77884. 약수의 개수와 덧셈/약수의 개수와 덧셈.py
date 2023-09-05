def solution(left, right):
    answer = 0
    for i in range(left,right+1):
        약수 = []
        for j in range(1,i+1):
            if i%j==0:
                약수.append(j)
        if len(약수)%2==1:
            answer-=i
        else:
            answer+=i
    return answer