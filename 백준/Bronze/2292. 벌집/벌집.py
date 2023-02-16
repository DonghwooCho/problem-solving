n = int(input())

target = 1
count = 1
while n > target:
    target += count * 6
    count += 1

print(count)
