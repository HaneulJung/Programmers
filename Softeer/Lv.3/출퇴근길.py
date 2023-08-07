import sys
sys.setrecursionlimit(10**6)

n, m = map(int, sys.stdin.readline().split())

route = [[] for _ in range(n+1)]
route_rev = [[] for _ in range(n+1)]

for _ in range(m):
    s, e = (map(int, sys.stdin.readline().split()))
    route[s].append(e)
    route_rev[e].append(s)
    
S, T = map(int, sys.stdin.readline().split())

def dfs(now, adj, visit):
    if visit[now] == 1:
        return
    visit[now] = 1
    for vtx in adj[now]:
        dfs(vtx, adj, visit)
    return

fromS = [0] * (n+1)
fromS[T] = 1
dfs(S, route, fromS)

fromT = [0] * (n+1)
fromT[S] = 1
dfs(T, route, fromT)

toS = [0] * (n+1)
dfs(S, route_rev, toS)

toT = [0] * (n+1)
dfs(T, route_rev, toT)

cnt = 0
for i in range(1, n+1):
    if fromS[i] and fromT[i] and toS[i] and toT[i]:
        cnt += 1

print(cnt-2)