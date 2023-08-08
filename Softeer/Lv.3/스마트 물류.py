import sys

N, K = map(int, sys.stdin.readline().split())

line = list(sys.stdin.readline().strip())

check = [i for i in range(-K, K+1)]

for i in range(N):
    if line[i] == 'P':       
        for c in check:
            pos = i + c
            if 0 <= pos < N and line[pos] == 'H':
                line[pos] = 'X'
                break

print(line.count('X'))