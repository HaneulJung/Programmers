def solution(name):
    alpha = ["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    answer = 0

    for i in range(len(name)):
        temp = alpha.index(name[i])           
        answer += min(temp, 26 - temp)   

    pos = 1
    temp = []
    while pos < len(name):
        if name[pos] == "A":
            s = pos
            c = 0
            while pos < len(name):
                if name[pos] == "A":
                    pos += 1
                    c += 1
                else:
                    break
            temp.append([s, c])
        pos += 1

    m = len(name) - 1
    for t in temp:
        a = (t[0]-1)*2 + len(name) - (t[0] + t[1])
        b = (len(name) - (t[0] + t[1]))*2 + t[0]-1

        m = min([m, a, b])

    answer += m

    return answer