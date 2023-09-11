from collections import deque

def solution(n, results):
    '''
    n명의 권투선수
    경기는 1대1 방식
    경기결과를 담은 2차원 배열 results
    [A,B] A선수가 B선수를 이겼다는 의미
    '''
    WIN = [[] for _ in range(n+1)]
    LOSE = [[] for _ in range(n+1)]
    
    for win, lose in results:
        WIN[win].append(lose)
        LOSE[lose].append(win)
    
    answer = 0
    
    for i in range(1, n+1):
        included_win = set()
        
        q = deque()
        q.append(i)
        while q:
            t = q.popleft()
            for w in WIN[t]:
                if w not in included_win:
                    included_win.add(w)
                    q.append(w)
                    
        included_lose = set()
        q = deque()
        q.append(i)
        while q:
            t = q.popleft()
            for l in LOSE[t]:
                if l not in included_lose:
                    included_lose.add(l)
                    q.append(l)
                      
        if len(included_win.union(included_lose)) == n - 1:
            answer += 1
    
    return answer