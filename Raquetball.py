import random

score1 = 0
score2 = 0
myserveprobability = 0.6
opponentserveprobability = 0.5
serve = True

games = [0]
wins = [0]

for a in range(1000):
    while score1 != 21 and score2 != 21:
        a = random.random()
        if serve == True:
            if a <= 0.6:
                score1 += 1
            else:
                serve = False
        else:
            if a <= 0.5:
                score2 += 1
            else:
                serve = True
    if score1 == 21:
        Win = True
    else:
        Win = False
    score1 = 0
    score2 = 0
    
    games.append(games[-1]+1)
    
    if Win == True:
        wins.append(wins[-1]+1)
    else:
        wins.append(wins[-1])

print(wins[-1] / games[-1])