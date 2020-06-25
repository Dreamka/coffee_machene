col = int(input().strip())
row = int(input().strip())

if col in (1, 8) and row in (1, 8):
    print(3)
elif col == 1 or col == 8 or row == 1 or row == 8:
    print(5)
else:
    print(8)
