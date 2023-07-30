def solution(elements):
    answer = set()
    
    for i in range(len(elements)):
        s = 0
        for j in range(1, len(elements)+1):
            s += elements[(i+j) % len(elements)]
            answer.add(s)
                
    return len(answer)