def getNum(day):
    return int(day.split(".")[0]) * 28 * 12 \
            + int(day.split(".")[1]) * 28 \
            + int(day.split(".")[2])
            
def solution(today, terms, privacies):
    today_num = getNum(today)
    
    due = {}    
    
    
    for term in terms:
        due[term.split(" ")[0]] = int(term.split(" ")[1]) * 28
    
    answer = []
    for idx, p in enumerate(privacies):
        if today_num - getNum(p.split(" ")[0]) >= due[p.split(" ")[1]]:
            answer.append(idx+1)
    return answer