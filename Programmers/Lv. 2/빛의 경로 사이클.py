def solution(grid):
    answer = []
    
    dy = len(grid)
    dx = len(grid[0])
    
    direction = [[1,0], [0,-1], [-1,0], [0,1]]
    
    visited = [[[False] * 4 for _ in range(dx)] for _ in range(dy)]
    
    for y in range(dy):
        for x in range(dx):
            for i in range(4):
                if visited[y][x][i] == True:
                    continue
                    
                count = 0
                ny, nx = y, x
                while not visited[ny][nx][i]:
                    visited[ny][nx][i] = True
                    count += 1
                    if grid[ny][nx] == "S": 
                        pass
                    elif grid[ny][nx] == "L": 
                        i = (i + 1) % 4
                    elif grid[ny][nx] == "R":
                        i = (i - 1) % 4
                    
                    ny = (ny + direction[i][1]) % dy 
                    nx = (nx + direction[i][0]) % dx
                    
                answer.append(count)
    
    return sorted(answer)