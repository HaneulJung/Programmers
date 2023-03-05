import math

def returnMinute(time):
    return int(time.split(":")[0]) * 60 + int(time.split(":")[1])

def solution(fees, records):
    answer = []
    
    dic = {}
    
    for record in records:
        r = record.split(" ") 
        if r[1] not in dic.keys():
            dic[r[1]] = [0, 0]
            
        if r[2] == "IN":
            dic[r[1]][0] -= returnMinute(r[0])
            dic[r[1]][1] = 1
        elif r[2] == "OUT":
            dic[r[1]][0] += returnMinute(r[0])
            dic[r[1]][1] = 0
    
    for carNumber, pay in sorted(dic.items()):
        if pay[1] == 1:
            pay[0] += returnMinute("23:59")
        
        if pay[0] <= fees[0]:
            answer.append(fees[1])
        else:
            answer.append(fees[1] + math.ceil((pay[0] - fees[0]) / fees[2]) * fees[3])
    return answer