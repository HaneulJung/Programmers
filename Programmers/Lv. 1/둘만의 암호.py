def solution(s, skip, index):
    alpha = ['a','b','c','d','e','f','g','h','i','j','k','l','m', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']
    for sk in skip:
        alpha.remove(sk)
    
    answer = ''
    
    for ss in s:
        answer += alpha[(alpha.index(ss) + index) % len(alpha)]    
    
    return answer