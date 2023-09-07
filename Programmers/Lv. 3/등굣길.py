# 집 (1,1)에서 학교 (m,n)으로 가는 길 구하기, m이 가로, n이 세로
# 물을 피해 갈 수 있는 최단 경로의 개수를 1,000,000,007로 나눈 나머지를 return

def solution(m, n, puddles):
    dp = [[0] * (m+1) for _ in range(n+1)]
    dp[1][1] = 1
    
    for i in range(1, n+1):
        for j in range(1, m+1):
            if i == 1 and j == 1:
                continue
                
            if [j,i] in puddles:
                dp[i][j] = 0
            else:
                dp[i][j] = (dp[i-1][j] + dp[i][j-1]) % 1000000007
                
    return dp[n][m]