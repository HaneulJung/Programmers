import sys


N, M = map(int, sys.stdin.readline().split())

standard = []
real = []

for _ in range(N):
    standard.append(list(map(int, sys.stdin.readline().split())))

for _ in range(M):
    real.append(list(map(int, sys.stdin.readline().split())))

standard_cnt = 0
standard_dis = 0

real_cnt = 0
real_dis = 0

max_diff = 0

for f in range(1, 101):
    if f > (standard_dis + standard[standard_cnt][0]):
        standard_dis += standard[standard_cnt][0]
        standard_cnt += 1

    if f > (real_dis + real[real_cnt][0]):
        real_dis += real[real_cnt][0]
        real_cnt += 1  

    diff = real[real_cnt][1] - standard[standard_cnt][1]
    if diff > 0 and diff > max_diff:
        max_diff = diff

print(max_diff)