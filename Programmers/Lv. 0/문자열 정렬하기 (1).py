def solution(my_string):
    answer = []
    for m in my_string:
        if m.isdigit():
            answer.append(int(m))
    return sorted(answer)