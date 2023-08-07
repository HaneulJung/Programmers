import sys

N = int(sys.stdin.readline())

rocks = list(map(int, sys.stdin.readline().split()))

dp = [1] * N

for i in range(N):
    cnt = 0
    for j in range(i):
        if rocks[j] < rocks[i]:
            cnt = max(cnt, dp[j]) 
    dp[i] = cnt + 1

print(max(dp))