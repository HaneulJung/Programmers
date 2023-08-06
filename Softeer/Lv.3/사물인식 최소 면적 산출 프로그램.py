import sys

N, K = map(int, sys.stdin.readline().split())

points = {}
for _ in range(N):
    x, y, k = map(int,sys.stdin.readline().split())
    if k not in points.keys():
        points[k] = []
        points[k].append([x,y])
    else:
        points[k].append([x,y])

minArea = 2000 * 2000
def dfs(color, left, right, top, bottom):
    global minArea
    if color == K + 1:
        minArea = min(minArea, (right-left)*(top-bottom))
        return
    
    for point in points[color]:
        left_temp = min(point[0], left)
        right_temp = max(point[0], right)
        top_temp = max(point[1], top)
        bottom_temp = min(point[1], bottom)
        if (right_temp-left_temp)*(top_temp-bottom_temp) < minArea:
            dfs(color+1, left_temp, right_temp, top_temp, bottom_temp)

dfs(1,1000,-1000,-1000,1000)
print(minArea)