def solution(numbers):
    # 가장 큰 수!
    # 모든 원수를 정렬해서 구할 시에는 총 자리수는 동일!
    # 즉 맨 앞자리 수가 크면 된다.
    # 문자열
    numbers = list(map(str,numbers))
    # 원소의 최대자리수까지 부풀려서 비교한다
    numbers.sort(key=lambda x : (x*4)[:4],reverse=True)
    return str(int("".join(numbers)))