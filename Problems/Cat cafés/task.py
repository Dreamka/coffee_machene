read = True

names = []
counts = []

while read:
    data = input().split()
    if data[0] == "MEOW":
        break
    names.append(data[0])
    counts.append(int(data[1]))

num = 0
for i in counts:
    if num < i:
        num = i
print(names[counts.index(num)])