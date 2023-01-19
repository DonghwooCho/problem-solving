# 1. 입력 받기
nums = input()
check = True if nums[0] == '-' else False

# 2. 최솟값 출력 하기
nums = nums.split('-')
for i in range(len(nums)):
    nums[i] = sum(list(map(int, nums[i].split('+'))))

print(-sum(nums) if check else 2 * nums[0] - sum(nums))