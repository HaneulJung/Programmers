def solution(matrix_sizes):
    INF = 10e9
    
    l = len(matrix_sizes)
    
    dp = [[INF] * l for _ in range(l)]
    
    # 2차원 행렬 dp의 요소 예를 들어 dp[i][j]는 i부터 j까지 행렬 곱에서의 최소값
    
    # dp[i][i] 요소는 0
    for i in range(l):
        dp[i][i] = 0
        
    for gap in range(1, l):
        for s in range(l - gap):
            e = s + gap
            
            for m in range(s,e):
                dp[s][e] = min(dp[s][e], \
                           dp[s][m] + dp[m+1][e] + matrix_sizes[s][0]*matrix_sizes[m][1]*matrix_sizes[e][1])
    
    return dp[0][-1]