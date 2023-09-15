def solution(numbers):
    # 가장 큰 수!
    # 모든 원수를 정렬해서 구할 시에는 총 자리수는 동일!
    # 즉 맨 앞자리 수가 크면 된다.
    # 문자열
    numbers = list(map(str,numbers))
    numbers.sort(key=lambda x : (x*4)[:4],reverse=True)
    numbers = "".join(numbers)
    if numbers=="0":
        return "0"
    while numbers[0]=="0":
        return str(int(numbers))
    return numbers