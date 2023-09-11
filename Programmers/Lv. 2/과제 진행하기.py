def convertToMinute(time):
    hour, minute = time.split(":")
    return int(hour) * 60 + int(minute)

def solution(plans):
    '''
    과제 하다가 새로운 과제 들어오면 새로운 과제부터
    과제 끝냈는데 하다가 만게 있으면 그거 하는데
    그 때 또 새로운 과제 들어오면 새로운 과제부터
    과제를 끝낸 순서대로 이름을 배열에 담아 return
    plan의 원소는 [name, start, playtime]
    '''
    
    # 시작 시간 순서대로 정렬
    plans.sort(key=lambda x : x[1])
    for plan in plans:
        plan[1] = convertToMinute(plan[1])
        plan[2] = int(plan[2])
    
    answer = []
    
    tmp = [[plans[0][0], plans[0][2]]]    # 이름과 소요시간
    
    for i in range(1, len(plans)):
        diffTime = plans[i][1] - plans[i-1][1]
        while diffTime > 0 and tmp:
            name, remainTime = tmp.pop()
            if diffTime >= remainTime:
                answer.append(name)
                diffTime -= remainTime
            else:
                tmp.append([name, remainTime - diffTime])
                break
        
        tmp.append([plans[i][0], plans[i][2]])
    
    while tmp:
        answer.append(tmp.pop()[0])
    
    return answer