from collections import deque

def solution(game_board, table):
    l = len(table)
    
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    
    def finding(arr, num):
        visited = [[False] * l for _ in range(l)]
        shapes = []
        for y in range(l):
            for x in range(l):          
                if arr[y][x] == num and not visited[y][x]:
                    q = deque()
                    q.append([y, x])
                    visited[y][x] = True
                    shape = []
                    while q:
                        cy, cx = q.popleft()
                        shape.append([cy, cx])
                        for move in moves:
                            dy = cy + move[0]
                            dx = cx + move[1]
                            if 0 <= dy < l and 0 <= dx < l and not visited[dy][dx]:
                                visited[dy][dx] = True
                                if arr[dy][dx] == num:
                                    q.append([dy, dx])
                    shapes.append(moveToZero(sorted(shape)))
        return shapes
    
    def moveToZero(arr):
        min_y, min_x = 50, 50
        tmp = []
        for y, x in arr:
            min_y = min(min_y, y)
            min_x = min(min_x, x)
        for y, x in arr:
            tmp.append([y - min_y, x - min_x])
        return tmp
    
    def rotation(arr):
        result = [arr]
        for _ in range(3):
            tmp = []
            for y, x in arr:
                tmp.append([x, -y])
            arr = moveToZero(sorted(tmp))
            result.append(arr)
        return result
            
    # table에서 블록 찾고 (0,0) 으로 이동
    blocks = finding(table, 1)
    # game_board에서 빈 곳 찾고 (0,0) 으로 이동
    spaces = finding(game_board, 0)
        
    answer = 0
    # 맞는 블록 찾기    
    q = deque()
    used = [i for i in range(len(blocks))]
    filled = [i for i in range(len(spaces))]
    q.append([used, filled])
    while q:
        _used, _filled = q.popleft()
        findFlag = False
        for i in _used:
            for j in _filled:
                if spaces[j] in rotation(blocks[i]):
                    _used.remove(i)
                    _filled.remove(j)
                    q.append([_used, _filled])
                    answer += len(blocks[i])
                    findFlag = True
                    break          
            if findFlag:
                break
                                       
    return answer