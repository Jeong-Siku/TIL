def solution(my_string, queries):
    answer = ''
    for i in range(len(queries)):
        start_idx = queries[i][0]
        end_idx = queries[i][1]+1
        before = my_string[start_idx:end_idx:]
        after = before[::-1]
        
        my_string = my_string[:start_idx] + after + my_string[end_idx:]
        
    return my_string