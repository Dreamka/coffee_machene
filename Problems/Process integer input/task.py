while True:
    number = int(input().strip())
    if number < 10:
        continue
    elif number > 100:
        break
    print(number)