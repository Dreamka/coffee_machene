a = int(input().strip())
b = int(input().strip())
h = int(input().strip())

print("Normal") if a < h < b else print("Deficiency") if h < a else print("Excess")