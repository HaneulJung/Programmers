from collections import deque

def check(str1, str2):
    c = 0
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            c += 1
    if c == 1:
        return True
    else:
        return False
    
def solution(begin, target, words):
    answer = 0
    
    if target not in words:
        return 0
    
    q = deque()
    q.append([begin, 0])
    while q:
        now, cnt = q.popleft()
        if now == target:
            return cnt
        
        for word in words:
            if check(now, word):
                q.append([word, cnt+1])
    
    return answer