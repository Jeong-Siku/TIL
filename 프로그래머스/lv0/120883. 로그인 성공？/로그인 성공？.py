def solution(id_pw, db):
    answer = ''
    # 일치
    # 완전탐색
    # 조건 : 아이디, 비밀번호 별도로
    for ID,password in db:
        if id_pw[0] == ID and id_pw[1]==password:
            return "login"
        elif id_pw[0] == ID:
            return "wrong pw"
    return "fail"