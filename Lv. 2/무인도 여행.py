from collections import deque

def solution(maps):
    answer = []
    
    go_row = [0, 0, 1, -1]
    go_column = [1, -1, 0, 0]
    
    row_len = len(maps)
    col_len = len(maps[0])
    
    visited = [[False for _ in range(col_len)] for _ in range(row_len)]    
    
    q = deque()
    
    for r in range(row_len):
        for c in range(col_len):
            if visited[r][c]:
                continue
            
            if maps[r][c] != "X":
                q.append([r, c])
                s = int(maps[r][c])
                visited[r][c] = True
                
                while q:
                    cur = q.popleft()
                    
                    for k in range(4):
                        nr = cur[0] + go_row[k]
                        nc = cur[1] + go_column[k]
                        if nc >= 0 and nc < col_len and nr >= 0 and nr < row_len and not visited[nr][nc]:
                            visited[nr][nc] = True
                            if maps[nr][nc] != "X":
                                q.append([nr, nc])
                                s += int(maps[nr][nc])
                answer.append(s)
    
    if len(answer) == 0:
        return [-1]
    
    return sorted(answer)