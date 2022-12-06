with open("input") as f:
    contents = f.read().split("\n")

pairs = [[[int(member) for member in pair.split('-')] for pair in item.split(',')] for item in contents]

def pair_subset(p1, p2):
    return (p1[0] <= p2[0] and p2[1] <= p1[1])

def check_subset(p1, p2):
    return pair_subset(p1, p2) or pair_subset(p2, p1)

def pair_partial_overlap(p1, p2):
    return p1[0] < p2[0] and p1[1] < p2[1] and p1[1] >= p2[0]

def check_partial_overlap(p1, p2):
    return pair_partial_overlap(p1, p2) or pair_partial_overlap(p2, p1)

total_subsets = 0
total_partials = 0
for pair in pairs:
    if check_subset(pair[0], pair[1]):
        total_subsets += 1
    if check_partial_overlap(pair[0], pair[1]):
        total_partials += 1

print(total_subsets)
print(total_partials)
print(total_partials + total_subsets)
