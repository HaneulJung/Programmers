def solution(s):
    answer = ''
    
    cap = True
    for ss in s:
        if ss == " ":
            cap = True
            answer += " "
            continue
        if ss != " " and cap:
            cap = False
            answer += ss.upper()
            continue
        answer += ss.lower()
        
    return answer