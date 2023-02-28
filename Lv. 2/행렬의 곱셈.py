def solution(arr1, arr2):
    answer = []
    
    n = len(arr1[0])
    m = len(arr2[0])
    
    for a1 in arr1:
        temp = []
        for i in range(m):
            s = 0
            for j in range(n):
                s += a1[j]*arr2[j][i]
            temp.append(s)
        answer.append(temp)
    return answer