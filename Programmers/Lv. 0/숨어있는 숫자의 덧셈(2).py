def solution(my_string):
    answer = 0
    number = ''
    
    for i in range(len(my_string)):
        if my_string[i].isdigit():            
            number += my_string[i]            
        else:
            if number == '':
                pass
            else:
                answer += int(number)
                number = ''    
    
    if number != '':
        answer += int(number)
        
    return answer