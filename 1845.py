def solution(nums):
    answer = 0
    temp = set(nums)
    if len(nums) < len(temp):
        answer = nums
    else:
        answer = temp
    return answer

nums = [3,1,2,3]
print(solution(nums))