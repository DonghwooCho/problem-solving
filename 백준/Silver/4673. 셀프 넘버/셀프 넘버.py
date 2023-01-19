res = [i + 1 for i in range(10000)]
for i in range(10000):
    temp = i
    temp_str = str(i)
    for j in range(len(temp_str)):
        temp += int(temp_str[j])
    if temp in res:
        res.remove(temp)

for element in res:
    print(element)