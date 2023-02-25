def solution(s):
    answer = 0
    
    temp = ["()", "[]", "{}"]
    
    for i in range(len(s)):
        t = s[i:] + s[:i]
        
        while len(t) != 0:
            isChanged = False
            for j in range(3):
                l1 = len(t)
                t = t.replace(temp[j], "")
                l2 = len(t)

                if l1 != l2:
                    isChanged = True
            if not isChanged:
                break
        if len(t) == 0:
            answer += 1
            
    return answer