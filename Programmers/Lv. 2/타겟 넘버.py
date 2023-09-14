def solution(numbers, target):
    answer = 0
    
    def dfs(idx, result):
        if idx == len(numbers):
            if result == target:
                nonlocal answer
                answer += 1                
                return
        else:
            dfs(idx+1, result+numbers[idx])
            dfs(idx+1, result-numbers[idx])
        
    dfs(0,0)
    
    return answer


from collections import deque

def solution(numbers, target):
    answer = 0
    
    q = deque()
    q.append([numbers[0], 0])
    q.append([-numbers[0], 0])
    while q:
        num, cnt = q.popleft()
        if cnt == len(numbers) - 1:
            if num == target:
                answer += 1
        else:
            cnt += 1
            q.append([num + numbers[cnt], cnt])
            q.append([num - numbers[cnt], cnt])
    
    
    return answer