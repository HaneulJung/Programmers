def solution(common):
    # 등차수열
    if (common[2] - common[1] == common[1] - common[0]):
        answer = common[-1] + common[1] - common[0]
        
    # 등비수열
    else:
        answer = common[-1] * (common[1] / common[0])
            
    return answer