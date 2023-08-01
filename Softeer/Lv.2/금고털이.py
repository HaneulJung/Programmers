import sys

W, N = map(int, sys.stdin.readline().split())

l = []

for _ in range(N):
    l.append(list(map(int, sys.stdin.readline().split())))

l.sort(key = lambda x : x[1], reverse=True)

c = 0
s = 0

while True:
    if W - l[c][0] > 0:
        s += (l[c][0] * l[c][1])
        W -= l[c][0]
        c += 1
    else:
        s += (W * l[c][1])
        print(s)
        break