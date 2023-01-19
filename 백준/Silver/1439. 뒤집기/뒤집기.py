S = input()

temp1 = S.split('0')
temp2 = S.split('1')

count1 = 0
count2 = 0
for i in temp1:
    if i:
        count1 += 1

for i in temp2:
    if i:
        count2 += 1

print(min(count1, count2))