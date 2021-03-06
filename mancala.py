BP1 = [4, 4, 4, 4, 4, 4, 0]
BP2 = [4, 4, 4, 4, 4, 4, 0]

def print_board():
    BP2.reverse()
    print('\nPocket # :  6  5  4  3  2  1')
    print('P2 -->', BP2[:1], BP2[1:7])
    print('P1 --> ', '  ', BP1[0:6],BP1[6:])
    print('Pocket # :  1  2  3  4  5  6')
    BP2.reverse()

print_board()

P1InPlay = sum(BP1[:6])
P2InPlay = sum(BP2[:6])

while (P1InPlay != 0) and (P2InPlay != 0):
    P1Move = int(input('Player 1, which pocket do you want to move?'))
    Stones = BP1[P1Move - 1]

    if BP1[P1Move-1] == 0:
        print('There are no stones in that pocket.TRY AGAIN')
        continue
    elif Stones + P1Move < 7:
        BP1[P1Move - 1] = 0
        for i in range(P1Move, Stones + P1Move):
            BP1[i] = BP1[i] + 1
        if (BP1[i] == 1) and (i != 6):
            BP1[6] = BP1[6] + BP2[5-i]  # adding to score
            BP2[5-i] = 0
            pass
        print_board()
    elif Stones + P1Move == 7:
        BP1[P1Move - 1] = 0
        for i in range(P1Move, Stones+P1Move):
            BP1[i] = BP1[i] + 1
        print_board()
        continue
    else:
        print('OF')
        OFlow = Stones + P1Move - 6

        for i in range(P1Move, 7):
            BP1[i] = BP1[i] + 1
        if OFlow < 7:
            BP1[P1Move - 1] = 0
            for i in range(0,OFlow-1):
                BP2[i] = BP2[i] + 1
            print_board()
        else:
            BP1[P1Move - 1] = 0
            for i in range(0, 6):
                BP2[i] = BP2[i] + 1
            for i in range(0,OFlow-7):
                BP1[i] = BP1[i] + 1
            if (BP1[i] == 1) and (i != 6):
                BP1[i] = BP1[i] + BP2[5-i]
                BP2[5-i] = 0
                pass
            print_board()

    P1InPlay = sum(BP1[:6])
    P2InPlay = sum(BP2[:6])

    while (P1InPlay != 0) and (P2InPlay != 0):
        P2Move = int(input('Player 2, which pocket do you want to move?'))
        Stones = BP2[P2Move - 1]

        if BP2[P2Move - 1] == 0:
            print('There are no stones in that pocket.TRY AGAIN')
            continue
        elif Stones + P2Move < 7:
            BP2[P2Move - 1] = 0
            for i in range(P2Move, Stones+P2Move):
                BP2[i] = BP2[i] + 1
            if (BP2[i] == 1) and (i != 6):
                BP2[6] = BP2[6] + BP1[5-i] # adding to score
                BP1[5-i] = 0
                pass
            print_board()
        elif Stones + P2Move == 7:
            BP2[P2Move - 1] = 0
            for i in range(P2Move, Stones+P2Move):
                BP2[i] = BP2[i] + 1
            print_board()
            continue
        else:
            print('OF')
            OFlow = Stones + P2Move - 6
            for i in range(P2Move, 7):
                BP2[i] = BP2[i] + 1
            if OFlow < 7:
                BP2[P2Move - 1] = 0
                for i in range(0,OFlow-1):
                    BP1[i] = BP1[i] + 1
            else:
                BP2[P2Move - 1] = 0
                for i in range(0, 6):
                    BP1[i] = BP1[i] + 1
                for i in range(0, OFlow - 5):
                    BP2[i] = BP2[i] + 1
                if (BP2[i] == 1) and (i != 6):
                    BP2[i] = BP2[i] + BP1[5-i]
                    BP1[5-i] = 0
                    pass
            print_board()
            P1InPlay = sum(BP1[:6])
            P2InPlay = sum(BP2[:6])
        break

print ('GAME OVER. Player 1 Scored: ', BP1[6], 'Player 2 Scored: ', BP2[6])

if BP1[6] >= BP2[6]:
    print("Player 1 wins")
else:
    print("Player 2 wins")