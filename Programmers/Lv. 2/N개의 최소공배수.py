# def solution(arr):
#     m = max(arr)
    
#     i = 1
#     while True:
#         flag = False
#         for a in arr:
#             if m * i % a == 0:
#                 pass
#             else:
#                 i += 1
#                 flag = True
#                 break
#         if not flag:
#             return (m*i)

import math

def solution(arr):
    answer = 1
    
    for a in arr:
        answer = (answer * a) / math.gcd(int(answer), a)
    
    return answer