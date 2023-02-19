from collections import deque
                
def findRoute(start, end, maps):
    row_len = len(maps)
    col_len = len(maps[0])   
    
    go_x = [1, -1, 0, 0]
    go_y = [0, 0, 1, -1]       
    
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    
    q = deque()
    q.append((start[0], start[1], 0))
    
    visited[start[0]][start[1]] = True
    
    distance = 0
    
    while q:
        cur = q.popleft()         
    
        for i in range(4):
            nx = cur[0] + go_x[i]
            ny = cur[1] + go_y[i]
            if (nx >= 0 and nx < row_len and ny >= 0 and ny < col_len):
                if visited[nx][ny] == False and maps[nx][ny] != "X":
                    visited[nx][ny] = True
                    q.append((nx, ny, cur[2] + 1))
                    if nx == end[0] and ny == end[1]:
                        return cur[2] +1    
    
    return -1   
    
def solution(maps):
    row_len = len(maps)
    col_len = len(maps[0])   
    
    for i in range(row_len):
        for j in range(col_len):
            if (maps[i][j] == "S"):
                start = (i, j)
            elif (maps[i][j] == "L"):
                lever = (i, j)
            elif (maps[i][j] == "E"):
                exit = (i, j)
    
    a = findRoute(start, lever, maps)
    b = findRoute(lever, exit, maps)
    
    if a == -1 or b == -1:
        return -1
    
    return a + b