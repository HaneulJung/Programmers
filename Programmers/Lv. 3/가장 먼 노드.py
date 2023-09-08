from collections import deque

def solution(n, edge):
    # n개의 노드, 간선 정보 edge
    lines = [[] for i in range(n+1)]
    for a, b in edge:
        lines[a].append(b)
        lines[b].append(a)
    
    distances = [-1] * (n+1)
    distances[1] = 0
    
    q = deque([1])
    while q:
        now = q.popleft()
        for node in lines[now]:
            if distances[node] == -1:
                print(node)
                distances[node] = distances[now] + 1
                q.append(node)
    
    return distances.count(max(distances))