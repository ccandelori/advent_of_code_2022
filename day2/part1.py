with open("input") as f:
    round_strings = f.read().split("\n")
    rounds = [
        [round for round in string.split(" ")] for string in round_strings
    ]

scoring = {'A': {'X':4, 'Y':8, 'Z':3}, 
           'B': {'X':1, 'Y':5, 'Z':9}, 
           'C': {'X':7, 'Y':2, 'Z':6}
          }

score = 0
for index, round in enumerate(rounds):
  score += scoring[round[0]][round[1]]

# Part 1
print(score)


# A X Rock ties with Rock, 1 point for rock, 3 points for draw       4
# B X Paper beats rock, 1 points for paper, 0 points for loss        5
# C X scissors lose to rock, 1 points for rock, 6 points for win     12
# C Y scissors beats paper, 2 points for paper, 0 points for loss    14
# B Y paper ties with paper, 2 points for paper, 3 points for draw   19