import sys

K, N = map(int, sys.stdin.readline().split())

operate = []
move_time = []
time = []

for i in range(N-1):
    line = list(map(int, sys.stdin.readline().split()))
    
    operate.append(line[:-1])
    move_time.append(line[-1])

line = list(map(int, sys.stdin.readline().split()))
operate.append(line)

for i in range(N-1):
    tmp = min(operate[i]) 

    for j in range(K):
        if i == j:
            operate[i+1][j] += operate[i][j]
        else:
            operate[i+1][j] += min(operate[i][j], tmp + move_time[i])

print(min(operate[-1]))