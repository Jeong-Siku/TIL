def solution(todo_list, finished):
    a = zip(todo_list,finished)
    return [todo for todo,ox in a if not ox]