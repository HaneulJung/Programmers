def getParent(parent, x):
    if parent[x] == x:
        return x
    return getParent(parent, parent[x])
    
def unionParent(parent, a, b):
    a = getParent(parent, a)
    b = getParent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, costs):
    answer = 0
    
    costs.sort(key=lambda x : x[2])
    
    parent = [i for i in range(n)]
    
    lineCnt = 0
    for cost in costs:
        n1, n2, c = cost
        if getParent(parent, n1) != getParent(parent, n2):
            answer += c
            lineCnt += 1
            
            unionParent(parent, n1, n2)
            
        if lineCnt == n - 1:
            break
    
    return answer