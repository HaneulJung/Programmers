import itertools

def solution(k, dungeons):    
    l = len(dungeons)
    t = list(itertools.permutations([i for i in range(l)]))
    
    answer = -1
    
    for tt in t:
        c = 0
        temp = k
        for ttt in tt:
            if dungeons[ttt][0] <= temp:
                c += 1
                temp -= dungeons[ttt][1]
            else:
                break
        answer = max(answer, c)                        
    
    return answer