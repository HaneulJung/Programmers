from collections import deque

def solution(n, computers):
    # 컴퓨터 개수 n, 연결에 대한 정보 computers
    answer = 0
    
    lines = [[] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if i == j:
                continue
            
            if computers[i][j] == 1:
                lines[i].append(j)
                
    visited = [False] * n   
    
    for i in range(n):  
        if not visited[i]:
            visited[i] = True
            q = deque()
            q.append(i)

            while q:
                n1 = q.popleft()
                for n2 in lines[n1]:
                    if not visited[n2]:
                        visited[n2] = True
                        q.append(n2)
            answer += 1
    
    return answer

    