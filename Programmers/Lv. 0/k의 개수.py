def solution(i, j, k):
    temp = ''
    for s in range(i,j+1):
        temp += str(s)
        
    return temp.count(str(k))