def solution(numbers):
    en = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(10):
        numbers = numbers.replace(en[i], str(i))
    return int(''.join(numbers))