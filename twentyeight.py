#!/usr/bin/env python3

import random
global trump, hearts, diamonds, spades, cloves, deck, p1, p2, p3, p4, table, trumpCard, team1, team2, plOrder
hearts = ["H-A", "H-7", "H-8", "H-9", "H-10", "H-J", "H-Q", "H-K"]
diamonds = ["D-A", "D-7", "D-8", "D-9", "D-10", "D-J", "D-Q", "D-K"]
spades = ["S-A", "S-7", "S-8", "S-9", "S-10", "S-J", "S-Q", "S-K"]
cloves = ["C-A", "C-7", "C-8", "C-9", "C-10", "C-J", "C-Q", "C-K"]
deck = ["H-A", "H-7", "H-8", "H-9", "H-10", "H-J", "H-Q", "H-K", "D-A", "D-7", "D-8", "D-9", "D-10", "D-J", "D-Q", "D-K", "S-A", "S-7", "S-8", "S-9", "S-10", "S-J", "S-Q", "S-K","C-A", "C-7", "C-8", "C-9", "C-10", "C-J", "C-Q", "C-K"]
trump = False
bid = 0
gameCounter = 0
p1 = []
p2 = []
p3 = []
p4 = []
table = []
trumpCard = "UNKNOWN"
team1 = 0
team2 = 0
plOrder = [1,2,3,4]

def deal(pL):
    cardNum = random.randint(0, len(deck)-1)
    card = deck[cardNum]
    pL.append(card)
    deck.remove(card)
    return card

def order(pl):
    if pl == 1:
        return [1,2,3,4]
    elif pl == 2:
        return [2,3,4,1]
    elif pl == 3:
        return [3,4,1,2]
    else:
        return [4,1,2,3]

def cardVal(card):
    if card == "H-A" or card == "D-A" or card == "S-A" or card == "C-A":
        return 1
    elif card == "H-10" or card == "D-10" or card == "S-10" or card == "C-10":
        return 1
    elif card == "H-0" or card == "D-9" or card == "S-9" or card == "C-9":
        return 2
    elif card == "H-J" or card == "D-J" or card == "S-J" or card == "C-J":
        return 3
    else:
        return 0
    
def cardTier(table, suit):
    if table.count(suit + "-J"):
        return table.index(suit + "-J")
    if table.count(suit + "-9"):
        return table.index(suit + "-9")
    if table.count(suit + "-A"):
        return table.index(suit + "-A")
    if table.count(suit + "-10"):
        return table.index(suit + "-10")
    if table.count(suit + "-K"):
        return table.index(suit + "-K")
    if table.count(suit + "-Q"):
        return table.index(suit + "-Q")
    if table.count(suit + "-8"):
        return table.index(suit + "-8")
    return table.index(suit + "-7")
    
def revealSuit(card):
    if hearts.count(card) == 1:
        return "HEARTS"
    elif diamonds.count(card) == 1:
        return "DIAMONDS"
    elif spades.count(card) == 1:
        return "SPADES"
    else:
        return "CLOVES"
    
def matchSuit(player, suit):
    vlist = []
    if player == 1:
        if suit == "HEARTS":
            for card in p1:
                if hearts.count(card) == 1:
                    vlist.append(card)
        elif suit == "DIAMONDS":
            for card in p1:
                if diamonds.count(card) == 1:
                    vlist.append(card)
        elif suit == "SPADES":
            for card in p1:
                if spades.count(card) == 1:
                    vlist.append(card)
        else:
            for card in p1:
                if cloves.count(card) == 1:
                    vlist.append(card)
    elif player == 2:
        if suit == "HEARTS":
            for card in p2:
                if hearts.count(card) == 1:
                    vlist.append(card)
        elif suit == "DIAMONDS":
            for card in p2:
                if diamonds.count(card) == 1:
                    vlist.append(card)
        elif suit == "SPADES":
            for card in p2:
                if spades.count(card) == 1:
                    vlist.append(card)
        else:
            for card in p2:
                if cloves.count(card) == 1:
                    vlist.append(card)
    elif player == 3:
        if suit == "HEARTS":
            for card in p3:
                if hearts.count(card) == 1:
                    vlist.append(card)
        elif suit == "DIAMONDS":
            for card in p3:
                if diamonds.count(card) == 1:
                    vlist.append(card)
        elif suit == "SPADES":
            for card in p3:
                if spades.count(card) == 1:
                    vlist.append(card)
        else:
            for card in p3:
                if cloves.count(card) == 1:
                    vlist.append(card)
    else:
        if suit == "HEARTS":
            for card in p4:
                if hearts.count(card) == 1:
                    vlist.append(card)
        elif suit == "DIAMONDS":
            for card in p4:
                if diamonds.count(card) == 1:
                    vlist.append(card)
        elif suit == "SPADES":
            for card in p4:
                if spades.count(card) == 1:
                    vlist.append(card)
        else:
            for card in p4:
                if cloves.count(card) == 1:
                    vlist.append(card)
    return vlist

def rWinner(table, pl):
    if trump == False:
        tempSuit = revealSuit(table[0])
        if tempSuit == "HEARTS":
            s = "H"
        elif tempSuit == "DIAMONDS":
            s = "D"
        elif tempSuit == "SPADES":
            s = "S"
        else:
            s = "C"
        winner = cardTier(table, s)
        return pl[winner]
    else:
        tempSuit = revealSuit(trumpCard)
        s = "NONE"
        for card in table:
            if tempSuit == "HEARTS":
                if hearts.count(card) == 1:
                    s = "H"
                    break
            elif tempSuit == "DIAMONDS":
                if diamonds.count(card) == 1:
                    s = "D"
                    break
            elif tempSuit == "SPADES":
                if spades.count(card) == 1:
                    s = "S"
                    break
            elif tempSuit == "CLOVES":
                if cloves.count(card) == 1:
                    s = "C"
                    break
            else:
                s = "NONE"
        if s != "NONE":
            winner = cardTier(table, s)
            return pl[winner]
        else:
            tSuit = revealSuit(table[0])
            if tSuit == "HEARTS":
                tS = "H"
            elif tSuit == "DIAMONDS":
                tS = "D"
            elif tSuit == "SPADES":
                tS = "S"
            else:
                tS = "C"
            winner = cardTier(table, tS)
            return pl[winner]
    
                

        
        
def cardValid(player, card):
    if hearts.count(card) == 0 and diamonds.count(card) == 0 and spades.count(card) == 0 and cloves.count(card) == 0 and card != "TRUMP":
        print("Error. Please play a valid card.")
        return False
    if player == 1:
        if p1.count(card) == 0 and card != "TRUMP":
            print("Error. Please play a valid card.")
            return False
        return True
    if player == 2:
        if p2.count(card) == 0 and card != "TRUMP":
            print("Error. Please play a valid card.")
            return False
        return True
    if player == 3:
        if p3.count(card) == 0 and card != "TRUMP":
            print("Error. Please play a valid card.")
            return False
        return True
    if player == 4:
        if p4.count(card) == 0 and card != "TRUMP":
            print("Error. Please play a valid card.")
            return False
        return True
    return True

def startValid(player, card):
    if player != plOrder[0]:
        return True
    if player == 1:
        if trump == True:
            return True
        if revealSuit(card) == revealSuit(trumpCard):
            print("Error. Cannot play the trump unless revealed.")
            return False
    return True 
    
def trumpCheck(player, card):
    global trumpCard
    global trump
    if card == "TRUMP":
        suit = revealSuit(table[0])
        vList = matchSuit(player, suit)
        if len(vList) == 0:
            trump = True
            if player == 1:
                print(trumpCard)
                table.append(trumpCard)
                print(p1)
                p1.remove(trumpCard)
                return True
            if player == 2:
                print(trumpCard)
                tsuit = revealSuit(trumpCard)
                vList = matchSuit(player, tsuit)
                if len(vList) == 0:
                    print("Error! No trump card found. Play another card")
                    return False
                while len(vList) > 0:
                    print(vList)
                    card = (input(str("Play a trump card ")))
                    if vList.count(card) == 0:
                        print("Error! Must play a valid trump card.")
                    else:
                        table.append(card)
                        p2.remove(card)
                        break
                return True
            if player == 3:
                print(trumpCard)
                tsuit = revealSuit(trumpCard)
                vList = matchSuit(player, tsuit)
                if vList == 0:
                    print("Error! No trump card found. Play another card")
                    return False
                while len(vList) > 0:
                    print(vList)
                    card = (input(str("Play a trump card ")))
                    if vList.count(card) == 0:
                        print("Error! Must play a valid trump card.")
                    else:
                        table.append(card)
                        p3.remove(card)
                        print(p3)
                        break
                return True
            if player == 4:
                print(trumpCard)
                suit = revealSuit(trumpCard)
                vList = matchSuit(player, suit)
                if vList == 0:
                    print("Error! No trump card found. Play another card")
                    return False
                while len(vList) > 0:
                    print(vList)
                    card = (input(str("Play a trump card ")))
                    if vList.count(card) == 0:
                        print("Error! Must play a valid trump card.")
                    else:
                        table.append(card)
                        p4.remove(card)
                        break
                return True
        print("Error! Cannot play the trump unless you are unable to play a valid card.")
        return False
    return True

def suitCheck(player, card):
    if player == plOrder[0]:
        return True
    if card == "TRUMP":
        return True
    print(table)
    suit = revealSuit(table[0])
    vList = matchSuit(player, suit)
    if len(vList) == 0:
        return True
    if vList.count(card) == 0:
        print("Error! Must play a card the same suit as the starter.")
        return False
    return True
        
def isValid(player, card):
    if cardValid(player, card) == False:
        return False
    if startValid(player, card) == False:
        return False
    if trumpCheck(player, card) == False:
        return False
    if suitCheck(player, card) == False:
        return False
    return True

def cRound(starter):
    global team1 
    global team2
    tRound = True
    if starter == 1:
        while tRound == True:
            print("Hello Player 1! Here is your current hand: ")
            print(p1)
            card = (input(str("Play a card: ")))
            if isValid(1, card) == True:
                table.append(card)
                p1.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 2! Here is your current hand: ")
            print(p2)
            card = (input(str("Play a card: ")))
            print(len(table))
            if isValid(2, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p2.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 3! Here is your current hand: ")
            print(p3)
            card = (input(str("Play a card: ")))
            if isValid(3, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p3.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 4! Here is your current hand: ")
            print(p4)
            card = (input(str("Play a card: ")))
            if isValid(4, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p4.remove(card)
                break
        nextSt = rWinner(table, plOrder)
        for card in table:
            if nextSt == 1 or nextSt == 3:
                team1 = team1 + cardVal(card)
            else:
                team2 = team2 + cardVal(card)
        return nextSt
    elif starter == 2:
        while tRound == True:
            print("Hello Player 2! Here is your current hand: ")
            print(p2)
            card = (input(str("Play a card: ")))
            if isValid(2, card) == True:
                table.append(card)
                p2.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 3! Here is your current hand: ")
            print(p3)
            card = (input(str("Play a card: ")))
            if isValid(3, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p3.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 4! Here is your current hand: ")
            print(p4)
            card = (input(str("Play a card: ")))
            if isValid(4, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p4.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 1! Here is your current hand: ")
            print(p1)
            card = (input(str("Play a card: ")))
            if isValid(1, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p1.remove(card)
                break
        
        nextSt = rWinner(table,plOrder)
        for card in table:
            if nextSt == 1 or nextSt == 3:
                team1 = team1 + cardVal(card)
            else:
                team2 = team2 + cardVal(card)
        return nextSt
    elif starter == 3:
        while tRound == True:
            print("Hello Player 3! Here is your current hand: ")
            print(p3)
            card = (input(str("Play a card: ")))
            if isValid(3, card) == True:
                table.append(card)
                p3.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 4! Here is your current hand: ")
            print(p4)
            card = (input(str("Play a card: ")))
            if isValid(4, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p4.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 1! Here is your current hand: ")
            print(p1)
            card = (input(str("Play a card: ")))
            if isValid(1, card) == True:
                if card == "TRUMP":
                     break
                table.append(card)
                p1.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 2! Here is your current hand: ")
            print(p2)
            card = (input(str("Play a card: ")))
            if isValid(2, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p2.remove(card)
                break
        
        nextSt = rWinner(table, plOrder)
        for card in table:
            if nextSt == 1 or nextSt == 3:
                team1 = team1 + cardVal(card)
            else:
                team2 = team2 + cardVal(card)
        return nextSt
        
    else:
        while tRound == True:
            print("Hello Player 4! Here is your current hand: ")
            print(p4)
            card = (input(str("Play a card: ")))
            if isValid(4, card) == True:
                table.append(card)
                p4.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 1! Here is your current hand: ")
            print(p1)
            card = (input(str("Play a card: ")))
            if isValid(1, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p1.remove(card)
                break
        
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 2! Here is your current hand: ")
            print(p2)
            card = (input(str("Play a card: ")))
            if isValid(2, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p2.remove(card)
                break
        print("The table is ")
        print(table)
        tRound = True
        while tRound == True:
            print("Hello Player 3! Here is your current hand: ")
            print(p3)
            card = (input(str("Play a card: ")))
            if isValid(3, card) == True:
                if card == "TRUMP":
                    break
                table.append(card)
                p3.remove(card)
                break
        
        nextSt = rWinner(table, plOrder)
        for card in table:
            if nextSt == 1 or nextSt == 3:
                team1 = team1 + cardVal(card)
            else:
                team2 = team2 + cardVal(card)
        return nextSt
        
        
        
for x in range(0, 4):
    deal(p1)
for x in range(0, 4):
    deal(p2)
for x in range(0, 4):
    deal(p3)
for x in range(0, 4):
    deal(p4)
    
while trump == False:
    print(p1)
    ans = (input(str("Enter how many points you would like to bid: ")))
    bid = int(ans)
    if bid < 14:
        print("Error: Minimum bid is 14.")
    elif bid > 28:
        print("Error: Maximum bid is 28.")
    else:
        break
        
while trump == False:
    ans = (input(str("Place the trump card here: ")))
    if hearts.count(ans) == 0 and diamonds.count(ans) == 0 and spades.count(ans) == 0 and cloves.count(ans) == 0 or p1.count(ans) == 0:
        print("Error. Please place a valid trump card.")
    else:
        trumpCard = ans
        break

for x in range(0, 4):
    deal(p1)
for x in range(0, 4):
    deal(p2)
for x in range(0, 4):
    deal(p3)
for x in range(0, 4):
    deal(p4)
    
while gameCounter < 8:
    starter = cRound(plOrder[0])
    plOrder = order(starter)
    table = []
    gameCounter = gameCounter + 1
    print(team1)
    print(team2)
    
if team1 >= bid:
    print("Team 1 wins!")
else:
    print("Team 2 wins!")




        
        
            