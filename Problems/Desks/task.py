group_1 = int(input())
group_2 = int(input())
group_3 = int(input())

tables_1 = int(group_1 / 2) + (group_1 % 2)
tables_2 = int(group_2 / 2) + (group_2 % 2)
tables_3 = int(group_3 / 2) + (group_3 % 2)

result = tables_1 + tables_2 + tables_3

print(result)