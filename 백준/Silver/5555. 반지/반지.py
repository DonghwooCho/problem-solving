target = input()
N = int(input())

count = 0
for i in range(N):
    string = input()
    temp = 1 if target in string else 0
    if temp:
         count += 1
         continue
    string = string[-len(target) - 2:] + string[:len(target)]
    temp = 1 if target in string else 0
    if temp:
         count += 1
         continue

print(count)