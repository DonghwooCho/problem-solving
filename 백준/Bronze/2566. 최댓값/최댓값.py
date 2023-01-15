arr = []
for i in range(9):
    arr.extend(list(map(int, input().split())))

target_idx = arr.index(max(arr))
print(max(arr))
print(target_idx // 9 + 1, target_idx % 9 + 1)