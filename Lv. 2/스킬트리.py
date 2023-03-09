def solution(skill, skill_trees):
    answer = 0
    
    dic = {}
    
    for skill_tree in skill_trees:
        for skil in skill:
            dic[skil] = False
            
        b = False
        for st in skill_tree:
            if st in skill:
                if False in list(dic.values())[:list(dic).index(st)]:
                    b = True
                    break
                else:
                    dic[st] = True
        if not b:
            answer += 1
        
    return answer


def solution(skill, skill_trees):
    answer = 0

    for skill_tree in skill_trees:
        skill_list = list(skill)
        for st in skill_tree:
            if st in skill:
                if st != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer