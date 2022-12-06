from collections import Counter
import numpy as np

with open("input") as f:
    contents = f.read().split("\n")

# Part 1
common_items = []
for item in contents:
    compartment1 = Counter(set(item[:int(len(item)/2)]))
    compartment2 = Counter(set(item[int(len(item)/2):]))

    common = compartment1 & compartment2
    common_items.append(list(common.elements())[0])

sum = 0
for item in common_items:
    if item.isupper():
        sum += ord(item) - ord('A') + 27
    else:
        sum += ord(item) - ord('a') + 1

print(sum)

# Part 2
trios = np.array_split(contents, len(contents)//3)
groups = []
for trio in trios:
    groups.append(list(trio))

print(groups)

badges = []
for group in groups:
    common = Counter(set(group[0])) & Counter(set(group[1])) & Counter(set(group[2]))
    badges.append(list(common)[0])

sum = 0
for badge in badges:
    if badge.isupper():
        sum += ord(badge) - ord('A') + 27
    else:
        sum += ord(badge) - ord('a') + 1

print(sum)