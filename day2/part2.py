with open("input") as f:
    round_strings = f.read().split("\n")
    rounds = [
        [round for round in string.split(" ")] for string in round_strings
    ]

scoring = {'A': {'X':3, 'Y':4, 'Z':8}, 
           'B': {'X':1, 'Y':5, 'Z':9}, 
           'C': {'X':2, 'Y':6, 'Z':7}
          }

score = 0
for index, round in enumerate(rounds):
  score += scoring[round[0]][round[1]]

# Part 2
print(score)


# X = lose
# Y = draw
# Z = win

# A X Rock beats scissors, 3 points for scissors, 0 points for loss            3
# B X Paper beats rock, 1 points for rock, 0 points for loss                   (+1) 4
# C X scissors beats paper, 2 points for paper, 0 points for loss              (+2) 6
# C Y scissors ties with scissors, 3 points for scissors, 3 points for draw    (+6) 12
# B Y paper ties with paper, 2 points for paper, 3 points for draw             (+5) 17