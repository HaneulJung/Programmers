def solution(n):
    nums = [0, 1]
    for i in range(1, n):
        nums.append(nums[i-1] + nums[i])
    
    return nums[-1] % 1234567