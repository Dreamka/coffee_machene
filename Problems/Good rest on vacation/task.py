duration = int(input().strip())
dayly_food = int(input().strip())
flight_cost = int(input().strip())
hotel_cost = int(input().strip())

print(((duration - 1) * hotel_cost) + (dayly_food * duration) + (flight_cost * 2))