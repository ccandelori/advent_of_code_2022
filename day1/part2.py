import sys
import time

start = time.time()

# input = open("input", "r").read().splitlines()

# current_calories = 0
# most_calories = [sys.maxsize]

# for i in input:
#     if i == "":
#         for index, value in enumerate(most_calories[-4:]):
#             if current_calories < value:
#                 most_calories.insert(index, current_calories)
#                 break
#         current_calories = 0
#     else:
#         current_calories += int(i)

# print(sum(most_calories[-4:-1]))


with open("input") as f:
    elf_inventories = f.read().split("\n\n")
    elf_inventories = [
        [int(snack) for snack in elf.split("\n")] for elf in elf_inventories
    ]

calories_carried = sorted([sum(elf) for elf in elf_inventories], reverse=True)

print(f"The top three elves are carrying {sum(calories_carried[:3])} calories.")

end = time.time()

print("Execution time:", (end - start) * 10**3, "ms")