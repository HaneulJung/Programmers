def solution(n, times):
    # 입국심사 기다리는 사람 수 n, 각 심사관이 한 명 심사하는데 걸리는 시간 배열 times
    
    def check(m):
        people = 0
        for time in times:
            people += (m // time)
        
        if people < n:
            return True
        else:
            return False
    
    def bSearch(s, e):
        m = (s + e) // 2
        
        if s == e:
            return s
    
        if check(m):
            return bSearch(m+1, e)
        else:
            return bSearch(s, m)
            
            
    return bSearch(1, max(times)*n)