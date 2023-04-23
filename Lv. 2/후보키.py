from itertools import combinations

def solution(relation):
    answer = 0
    
    row = len(relation)
    col = len(relation[0])
    
    cols = [i for i in range(col)]
    
    combs = []
    for i in range(1 ,col+1):
        combs.extend(combinations(cols, i))
    
    results = []
    
    for comb in combs:   
        dict_temp = {}
        for r in range(row): 
            key = tuple([relation[r][c] for c in comb])
            if key not in dict_temp.keys():
                dict_temp[key] = True
            else:
                break
                
            if len(dict_temp) == row:
                put = True
                for x in results:
                    if set(x).issubset(set(comb)):
                        put = False
                        break
                if put:
                    results.append(comb)
                    answer += 1
    
    return answer