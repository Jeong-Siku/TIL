def solution(numbers):
    result = numbers
    alp = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    num = ["0","1","2","3","4","5","6","7","8","9"]
    for i in range(len(alp)):
        if alp[i] in result:
            result = result.replace(alp[i],num[i])
    return int(result)

