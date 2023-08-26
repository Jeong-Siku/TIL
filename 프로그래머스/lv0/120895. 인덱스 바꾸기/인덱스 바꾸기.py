def solution(my_string, num1, num2):
    answer = ''
    my_string = [i for i in my_string]
    my_string[num2],my_string[num1] =my_string[num1],my_string[num2]
    return "".join(my_string)