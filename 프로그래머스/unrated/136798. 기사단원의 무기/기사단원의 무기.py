def solution(number, limit, power):
    answer = 0
    # 약수
    # 제한수치
    # 대치
    for i in range(1,number+1):
        약수 = []
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                약수.append(j)
                if j**2 != i:
                    약수.append(i//j)
        dmg = len(약수)
        if dmg<=limit:
            answer+=dmg
        else:
            answer+=power
            
    return answer