from collections import deque

def solution(x, y, n):
    
    if x == y:
        return 0
        
    check = [False] * (y + 1)
    
    q = deque()
    q.append([x, 0])
    
    while q:        
        cur_x, c = q.popleft()
        
        if cur_x == y:
            return c
        
        if cur_x + n <= y and not check[cur_x + n]:
            check[cur_x + n] = True
            q.append([cur_x + n, c + 1])
        
        if cur_x * 2 <= y and not check[cur_x * 2]:
            check[cur_x * 2] = True
            q.append([cur_x * 2, c + 1])
            
        if cur_x * 3 <= y and not check[cur_x * 3]:
            check[cur_x * 3] = True
            q.append([cur_x * 3, c + 1])
    
    return -1