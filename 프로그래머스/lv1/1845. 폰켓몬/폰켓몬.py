def solution(nums):
    answer = 0
    num_type = list(set(nums))
    sel_num = len(nums)/2
    if sel_num>len(num_type):
        return len(num_type)
    return sel_num