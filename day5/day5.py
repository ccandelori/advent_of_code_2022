import time

start = time.time()

with open("input") as f:
    contents = f.read().split("\n\n")

# Separate begin state from instructions
begin_state, instructions = contents[0].split('\n')[:-1], contents[1].split('\n')
begin_state = [
    [(item[idx:idx+3]) for idx in range(0, len(item), 4)] for item in begin_state
]

stacks = [item for item in zip(*begin_state[::-1])]
stacks2 = [item for item in zip(*begin_state[::-1])]

for i in stacks: print(i)

# Rearrange stacks for easier manipulation
# stacks = [[] for _ in range(len(begin_state[0]))]
# stacks2 = [[] for _ in range(len(begin_state[0]))]
# for stack in begin_state:
#     for index, crate in enumerate(stack):
#         if crate != '   ':
#             stacks[index].insert(0, crate)
#             stacks2[index].insert(0, crate)

# Filter out strings from instructions
for index, instruction in enumerate(instructions):
    instruction = instruction.split(" ")
    del instruction[::2]
    instructions[index] = [int(item) for item in instruction]

# Move crates
for crates, origin, destination in instructions:
    # Part 1
    for _ in range(crates):
        stacks[destination - 1].append(stacks[origin - 1].pop(-1))

    # Part 2
    stacks2[destination - 1] += stacks2[origin - 1][-crates:]
    del stacks2[origin - 1][-crates:]


for stack in stacks: print(stack[-1])
print('')
for stack in stacks2: print(stack[-1])

end = time.time()

print("Execution time:", (end - start) * 10**3, "ms")