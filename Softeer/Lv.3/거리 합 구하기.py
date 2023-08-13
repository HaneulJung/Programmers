import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline

N = int(input())

if N == 1:
    print(0)
else:
    line = {}
    for _ in range(N-1):
        x, y, t = map(int, input().split())
        if x not in line.keys():
            line[x] = []
        if y not in line.keys():
            line[y] = []
        line[x].append([y, t])
        line[y].append([x, t])

    subTreeCnt = [1] * (N+1)
    distSum = [0] * (N+1)

    def dfs1(current, parent):
        for y, t in line[current]:
            if y != parent:
                dfs1(y, current)
                distSum[current] += distSum[y] + subTreeCnt[y]*t
                subTreeCnt[current] += subTreeCnt[y]
        return


    def dfs2(current, parent):
        for y, t in line[current]:
            if y != parent:
                distSum[y] = distSum[current] + t*(N - 2*subTreeCnt[y])
                dfs2(y, current)
        return

    dfs1(1,1)
    dfs2(1,1)

    for i in range(1, N+1):
        print(distSum[i])