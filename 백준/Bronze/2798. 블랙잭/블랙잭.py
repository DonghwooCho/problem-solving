# 1. 입력 받기
N, M = map(int, input().split())
nums = list(map(int, input().split()))

# 2. M보다 크지 않으면서 M에 가까운 숫자 3개의 합 출력
res = []
for i in range(N - 2):
    for j in range(i + 1, N - 1):
        for k in range(j + 1, N):
            if M >= nums[i] + nums[j] + nums[k]:
                res.append(nums[i] + nums[j] + nums[k])

print(max(res))