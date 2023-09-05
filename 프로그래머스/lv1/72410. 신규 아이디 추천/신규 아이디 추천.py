import re
def solution(new_id):
    # 조건 : 아이디 3~15, -, _, .
    new_id = new_id.lower()
    
    new = ""
    for i in new_id:
        if i.isdigit() or i.isalpha() or i=="." or i=="-" or i=="_":
            new+=i
    new_id = new
    
    while ".." in new_id:
        new_id = new_id.replace("..",".")
    
    # 인덱스는 빈 문자열일 경우 범위 에러가 나온다.
    # startswith 또는 endswith쓸 것

    
    if new_id[0] ==".":
        new_id = new_id[1:] if len(new_id)>1 else "."
    if new_id[-1] ==".":
        new_id = new_id[:-1] 
    
    print(new_id)
    # while new_id.startswith(".") or new_id.endswith("."):
    #     if new_id.startswith("."):
    #         new_id = new_id[1:]
    #     if new_id.endswith("."):
    #         new_id = new_id[:-1]

    if new_id =="":
        new_id ="a"
        
    if len(new_id) >=16:
        new_id = new_id[:15]
        if new_id[-1]==".":
            new_id = new_id[:-1]
            
    if len(new_id)<=2:
        while len(new_id)!=3:
            new_id=new_id + new_id[-1]
            
    return new_id