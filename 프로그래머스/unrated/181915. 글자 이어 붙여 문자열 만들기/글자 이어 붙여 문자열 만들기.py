# def solution(my_string, index_list):
#     answer = ''
#     for i in index_list:
#         answer+=my_string[i]
#     return answer

def solution(my_string, index_list):
    return ''.join([my_string[i] for i in index_list])