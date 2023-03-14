from collections import deque

def solution(maps):
    col_len = len(maps[0])
    row_len = len(maps)
    
    move = [(1,0), (-1,0), (0,1), (0,-1)]
    
    x, y = 0, 0
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]
    visited[x][y] = True
    
    queue = deque([[x, y, 1]])
    
    distance = []
    
    while queue:
        q = queue.popleft()
        for i in range(4):
            nx, ny = q[0] + move[i][0], q[1] + move[i][1]
            
            if nx == row_len -1 and ny == col_len - 1:
                distance.append(q[2] + 1)
            
            if nx >= 0 and nx < row_len and ny >= 0 and ny < col_len and not visited[nx][ny]:
                if maps[nx][ny] == 1:
                    queue.append([nx, ny, q[2] + 1])
                    visited[nx][ny] = True
                                 
    if len(distance) == 0:
        return -1
    else:
        return min(distance)