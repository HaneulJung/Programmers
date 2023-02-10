def solution(numbers, direction):
    if direction == 'left':
        num = numbers[0]
        numbers[0:-1] = numbers[1:]
        numbers[-1] = num
    else:
        num = numbers[-1]
        numbers[1:] = numbers[:-1]
        numbers[0] = num
    return numbers