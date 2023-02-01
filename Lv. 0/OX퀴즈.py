def solution(quiz):
    
    answer = []
    
    for q in quiz:
        s = q.split(" ")
        if (s[1] == "-"):
            if (int(s[0]) - int(s[2]) == int(s[-1])):
                answer.append("O")
            else:
                answer.append("X")
        elif (s[1] == "+"):
            if (int(s[0]) + int(s[2]) == int(s[-1])):
                answer.append("O")
            else:
                answer.append("X")
    
    return answer