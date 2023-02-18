def solution(survey, choices):
    score = [-3, -2, -1, 0, 1, 2, 3]
    
    dic = { 'R':0, 'T':0, 'C':0, 'F':0, 'J':0, 'M':0, 'A':0, 'N':0}
    
    for i in range(len(survey)):
        dic[survey[i][-1]] += score[choices[i]-1]
    
    answer = ''
    
    if dic['R'] >= dic['T']:
        answer += "R"
    else:
        answer += "T"
    
    if dic['C'] >= dic['F']:
        answer += "C"
    else:
        answer += "F"
        
    if dic['J'] >= dic['M']:
        answer += "J"
    else:
        answer += "M"
        
    if dic['A'] >= dic['N']:
        answer += "A"
    else:
        answer += "N"
        
    return answer