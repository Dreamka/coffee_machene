scores = input().split()

fails = 0
corrects = 0
for i in scores:
    if fails == 3:
        print("Game over")
        print(corrects)
        break
    if i == "C":
        corrects += 1
    if i == "I":
        fails += 1
else:
    print("You won")
    print(corrects)