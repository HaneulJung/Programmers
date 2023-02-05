def solution(id_pw, db):
    
    for d in db:
        if d[0] == id_pw[0]:
            if d[1] == id_pw[1]:
                return "login"
            else:
                return "wrong pw"
    return "fail"