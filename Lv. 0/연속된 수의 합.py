def sum(num):
    s = 0
    for i in range(num):
        s += i
    return s

def solution(num, total):
    a = (total - sum(num)) / num
    
    answer = []
    for i in range(num):
        answer.append(a + i)
    return answer