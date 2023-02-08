def solution(num_list):
    count = 0
    for n in num_list:
        if n % 2 == 0:
            count += 1
    return [count, len(num_list)-count]