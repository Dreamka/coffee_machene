square_sum = 0
sum_ = 0
count = 0

while True:
    dig = int(input().strip())
    sum_ += dig
    square_sum += dig ** 2
    if sum_ == 0:
        break

print(square_sum)
