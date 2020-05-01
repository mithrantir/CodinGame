def card_value(card):
    if len(card) == 3:
        return 10
    elif card[0] == 'J':
        return 11
    elif card[0] == 'Q':
        return 12
    elif card[0] == 'K':
        return 13
    elif card[0] == 'A':
        return 14
    else:
        return int(card[0])


n = int(input())  # the number of cards for player 1
hand1 = []
for i in range(n):
    hand1.append(card_value(input()))  # the n cards of player 1

m = int(input())  # the number of cards for player 2
hand2 = []
for i in range(m):
    hand2.append(card_value(input()))  # the m cards of player 2

draw, turn = False, 0
war_hand1, war_hand2 = [], []
while len(hand1) > 0 and len(hand2) > 0:

    c1, c2 = hand1.pop(0), hand2.pop(0)
    if len(war_hand1) == 0:
        turn = turn + 1
    if c1 > c2:
        while len(war_hand1) > 0:
            hand1.append(war_hand1.pop(0))
        hand1.append(c1)
        while len(war_hand2) > 0:
            hand1.append(war_hand2.pop(0))
        hand1.append(c2)
    elif c2 > c1:
        while len(war_hand1) > 0:
            hand2.append(war_hand1.pop(0))
        hand2.append(c1)
        while len(war_hand2) > 0:
            hand2.append(war_hand2.pop(0))
        hand2.append(c2)
    else:
        if len(hand1) < 4 or len(hand2) < 4:
            draw = True
            break
        war_hand1.append(c1)
        war_hand2.append(c2)
        for i in range(3):
            war_hand1.append(hand1.pop(0))
            war_hand2.append(hand2.pop(0))

if draw:
    print("PAT")
elif len(hand1) == 0:
    print("2 {}".format(turn))
else:
    print("1 {}".format(turn))
