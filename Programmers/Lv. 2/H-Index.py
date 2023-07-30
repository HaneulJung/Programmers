# def solution(citations):
#     for i in range(max(citations), -1, -1):
#         if len(list(filter(lambda x : x >= i, citations))) >= i:
#             return i
        
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer
