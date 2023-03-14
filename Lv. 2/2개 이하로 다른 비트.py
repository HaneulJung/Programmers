def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            s = number + 1
            while True:
                if bin(number ^ s).count("1") <= 2:
                    answer.append(s)
                    break
                else:
                    s += 1
            
    return answer

def solution(numbers):
    answer = []
    
    for number in numbers:
        if number % 2 == 0:
            answer.append(number+1)
        else:
            b = '0' + bin(number)[2:]
            idx = b.rfind('0')
            b = list(b)
            b[idx] = '1'
            b[idx+1] = '0'
            answer.append(int(''.join(b), 2))
            
    return answer