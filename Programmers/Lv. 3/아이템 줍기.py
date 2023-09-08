from collections import deque

def solution(rectangle, characterX, characterY, itemX, itemY):
    '''
    지형을 나타내는 직사각형 담긴 2차원 배열 rectangle [좌측하단x, 좌측하단y, 우측상단x, 우측상단y]
    초기 캐릭터 위치 characterX, characterY
    아이템 위치 itemX, itemY
    '''  
    moves = [(1,0), (-1,0), (0,1), (0,-1)]
    
    # 만약 ㄷ 모양 테두리가 있으면 테두리로 가지 않고 
    # 바로 올라가는 경우가 생기기 때문에 2배를 해서 field를 생성하는 것
    inField = []
    for lx, ly, rx, ry in rectangle:
        for i in range(lx*2+1, rx*2):
            for j in range(ly*2+1, ry*2):
                inField.append([i, j])
    
    outField = []
    for lx, ly, rx, ry in rectangle:
        for i in range(lx*2, rx*2+1):
            if [i, ly * 2] not in inField:
                outField.append([i, ly * 2])
            if [i, ry * 2] not in inField:
                outField.append([i, ry * 2])
        for i in range(ly*2+1, ry*2):
            if [lx * 2, i] not in inField:
                outField.append([lx*2, i])
            if [rx * 2, i] not in inField:
                outField.append([rx*2, i])
                    
    q = deque()
    q.append([[characterX*2, characterY*2], 0])
    
    visited = []
    visited.append([characterX*2, characterY*2])
    while q:
        pos, cnt = q.popleft()
        if pos == [itemX*2, itemY*2]:
            return cnt / 2
        for move in moves:
            dx = pos[0] + move[0]
            dy = pos[1] + move[1]
            if [dx, dy] not in visited and [dx, dy] in outField:
                visited.append([dx, dy])
                q.append([[dx, dy], cnt+1])