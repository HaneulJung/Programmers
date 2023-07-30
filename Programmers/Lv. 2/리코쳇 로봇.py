from collections import deque

def solution(board):
    col = len(board)
    row = len(board[0])
    
    sh, sv = 0, 0
    for c in range(col):
        for r in range(row):
            if board[c][r] == "R":
                sh = c
                sv = r
                break
    
    q = deque()
    q.append([(sh, sv), 0])
    route = [(sh, sv)]
    
    while q:
        pos = q.popleft()
        ch, cv, count = pos[0][0], pos[0][1], pos[1]

        if board[ch][cv] == "G":
            return count
        
        for direction in [[1,0], [-1,0], [0,1], [0,-1]]:
            mh, mv = ch, cv
            while mh >= 0 and mh < col and mv >= 0 and mv < row:
                if board[mh][mv] == "D":
                    break
                mh += direction[0]
                mv += direction[1]
            if ch + direction[0] == mh and cv + direction[1] == mv:
                pass
            else:    
                if (mh - direction[0], mv - direction[1]) not in route:
                    q.append([(mh - direction[0], mv - direction[1]), count + 1])
                    route.append((mh - direction[0], mv - direction[1]))
    
    return -1