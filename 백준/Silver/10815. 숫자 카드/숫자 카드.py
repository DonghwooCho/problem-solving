# 1. Input data
N = int(input())
nums = list(map(int, input().split()))
M = int(input())
targets = list(map(int, input().split()))

# 2. Check nums
nums_set = set(nums)
targets_set = set(targets)

intersection_set = nums_set & targets_set

# 3. Output results
for target in targets:
    print(1 if target in intersection_set else 0, end=' ')
    