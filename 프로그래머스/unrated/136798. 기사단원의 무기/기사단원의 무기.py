def solution(number, limit, power):
    answer = 0
    # 약수 => 제곱근으로 시간 줄이기
    # 제한수치
    # 대치
    for i in range(1,number+1):
        약수 = []
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                약수.append(j)
                # 제곱근일 경우 추가로 더해지는 것을 방지. 다른 방법으로 set 활용 가능
                if j**2 != i:
                    약수.append(i//j)
        dmg = len(약수)
        if dmg<=limit:
            answer+=dmg
        else:
            answer+=power
            
    return answer

def solution(number, limit, power):
    answer = 0
    # 약수 => 제곱근으로 시간 줄이기
    # 제한수치
    # 대치
    for i in range(1,number+1):
        약수 = []
        for j in range(1,int(i**0.5)+1):
            if i%j==0:
                약수.append(j)
                약수.append(i//j)
        dmg = len(set(약수))
        if dmg<=limit:
            answer+=dmg
        else:
            answer+=power
            
    return answer