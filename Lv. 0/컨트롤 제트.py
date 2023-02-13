def solution(s):
    answer = 0
    
    for n in s.split(" "):
        if n == "Z":
            answer -= int(temp)
        else:            
            answer += int(n)
            temp = n
            
    return answer