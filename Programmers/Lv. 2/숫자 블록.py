def solution(begin, end):
    '''
    숫자 0이 적힌 블록들 위에 다른 숫자가 적힌 블록들을 설치
    블록 번호가 n일 때 가장 첫 블록은 n*2 위치에 설치, 그 다음은 n*3, n*4 ...
    기존에 설치된 블록은 빼고 새로운 블록 설치
    길이가 1,000,000,000인 도로에 1부터 10,000,000까지 숫자가 적힌 블록을 설치
    begin ~ end 구간의 블록들을 return
    '''    
    # 각 번호에 들어갈 블록 숫자는 번호의 약수 중 가장 큰 거
    
    answer = []
    
    def find(num):
        tmp = 1
        for n in range(2, int(num**0.5)+1):
            if num % n == 0:
                if num // n <= 10000000:
                    return num // n
                else:
                    tmp = n
        return tmp
    
    for i in range(begin, end + 1):
        if i == 1:
            answer.append(0)
        else:
            answer.append(find(i))
    return answer
