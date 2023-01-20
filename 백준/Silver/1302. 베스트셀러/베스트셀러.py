from collections import Counter

n = int(input())
books = {}
for i in range(n):
    book = input()
    if book in books.keys():
        books[book] += 1
    else:
        books[book] = 1

temp = sorted(books.items(), key = lambda x: x[1], reverse = True)
res = []
for i in temp:
    if i[1] == temp[0][1]:
        res.append(i[0])

res.sort()
print(res[0])