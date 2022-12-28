# 1. 입력 받기
T = int(input())

test_cases = []
for i in range(T):
    test_cases.append(input())

# 2. 출력 하기
for test_case in test_cases:
    print(test_case[0], test_case[-1], sep="")