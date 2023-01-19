n, m = input().split()

count1 = 0
for i in list(n):
    count1 += int(i)

count2 = 0
for i in list(m):
    count2 += int(i)
    
print(count1 * count2)