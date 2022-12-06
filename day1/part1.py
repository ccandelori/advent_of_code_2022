input = open("input", "r").read().splitlines()

calorie_count = 0
most_calories = 0

for value in input:
    if value == "":
        if calorie_count > most_calories:
            most_calories = calorie_count
        calorie_count = 0
    else:
        calorie_count += int(value)

print(most_calories)