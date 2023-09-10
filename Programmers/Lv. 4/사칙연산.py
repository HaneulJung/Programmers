def solution(arr):
    '''
    문자열 형태의 숫자, +, - 가 들어있는 배열 arr
    서로 다른 연산 순서의 계산 결과 중 최댓값 return
    '''
    
    nums = []
    ops = []
    for i, a in enumerate(arr):
        if i % 2 == 0:
            nums.append(int(a))
        else:
            ops.append(a)
    
    N = len(nums)
    dp_max = [[-2001] * N for _ in range(N)]
    dp_min = [[2001] * N for _ in range(N)]
    
    for i in range(N):
        dp_max[i][i] = nums[i]
        dp_min[i][i] = nums[i]
        
    for d in range(1, N):
        for s in range(N - d):
            e = s + d
            
            for m in range(s, e):
                if ops[m] == "+":
                    dp_max[s][e] = max(dp_max[s][m] + dp_max[m+1][e], dp_max[s][e])
                    dp_min[s][e] = min(dp_min[s][m] + dp_min[m+1][e], dp_min[s][e])
                else:
                    dp_max[s][e] = max(dp_max[s][m] - dp_min[m+1][e], dp_max[s][e])
                    dp_min[s][e] = min(dp_min[s][m] - dp_max[m+1][e], dp_max[s][e])
            
    return dp_max[0][-1]