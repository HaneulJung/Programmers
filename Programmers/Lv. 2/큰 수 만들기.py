# def solution(number, k):
#     answer = ''    
    
#     l = len(number) - k
    
#     while l != 0:
#         for n in sorted(list(number), reverse=True):
#             if len(number[number.index(n):]) >= l:
#                 answer += n
#                 l -= 1
#                 number = number[number.index(n)+1:]
#                 break        
    
#     return answer

def solution(number, k):    
    
    stack = [number[0]]
    
    for n in number[1:]:
        while k > 0 and stack and stack[-1] < n:
            stack.pop(-1)
            k -= 1
        stack.append(n)
        
    return ''.join(stack[:len(number) - k])