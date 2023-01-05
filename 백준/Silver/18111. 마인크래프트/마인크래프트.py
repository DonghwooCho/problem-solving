import sys

# 1. 입력 받기
N, M, B = map(int, sys.stdin.readline().split())

location_map = [0] * N
for i in range(N):
    location_map[i] = list(map(int, sys.stdin.readline().split()))

# 2. 땅을 고르는 데 걸리는 시간과 높이 구하기(완전 탐색, brute force)
answer_time = N * M * 256 * 2
answer_floor = 0
for floor in range(257):
    block_for_up = 0
    block_for_down = 0

    for i in range(N):
        for j in range(M):
            if location_map[i][j] >= floor:
                block_for_down += location_map[i][j] - floor
            else:
                block_for_up += floor - location_map[i][j]
    
    # floor 만큼 층을 세우기 위한 조건
    if block_for_down + B >= block_for_up:
        res = (block_for_down * 2) + block_for_up

# 3. 시간이 최소일 때, 시간과 높이 구하기 
        if res <= answer_time:
            answer_time = res
            answer_floor = floor

print(answer_time, answer_floor)
    