count_ = int(input().strip())

i = 0
while i < count_:
    n = int(input().strip())
    if n % 7 == 0:
        print(n ** 2)
    i += 1
