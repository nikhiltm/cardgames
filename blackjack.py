#!/usr/bin/env python3

import random
global diamonds, hearts, spades, cloves, deck
diamonds = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
hearts = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
spades = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
cloves = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
deck = [diamonds, hearts, spades, cloves]
playerHand = []
dealerHand = []
plTotal = 0
dlTotal = 0
plStand = False
dlStand = False
start = True
game = True
winner = 0

def changeAce(pl, total):
    counter = pl.count("A")
    if counter >= 1 and total > 21:
        while total > 21 and counter > 0:
            total = total - 10
            counter = counter - 1
    return total
            
def cardVal(card):
    if card == "A":
        return 11
    elif card == "J" or card == "Q" or card == "K":
        return 10
    else:
        return int(card)

def drawCard(pL):
    suitNum = random.randint(0, len(deck)-1)
    cardNum = random.randint(0, len(deck[suitNum])-1)
    card = deck[suitNum][cardNum]
    print(card)
    pL.append(card)
    deck[suitNum].remove(card)
    return card

while start == True:
    card = drawCard(playerHand)
    plTotal = plTotal + cardVal(card)
    card = drawCard(dealerHand)
    dlTotal = dlTotal + cardVal(card)
    if plTotal != 21 or dlTotal != 21:
        break
    else:
        diamonds = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        hearts = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        spades = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        cloves = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        deck = [diamonds, hearts, spades, cloves]
        plTotal = 0
        dlTotal = 0

if plTotal == 21:
    print("Congratulations! You have won the game!")
elif dlTotal == 21:
    print("The house has won")
else:
    while game == True:
        print("Your current hand is: ")
        print(playerHand)
        if plTotal <= 11:
            card = drawCard(playerHand)
            plTotal = plTotal + cardVal(card)
        else:
            while plStand == False:
                ans = (input(str("Would you like to hit or stand? ")))
                if ans != "HIT" and ans != "STAND":
                    print("Error! Please choose to hit or stand.")
                elif ans == "HIT":
                    card = drawCard(playerHand)
                    plTotal = plTotal + cardVal(card)
                    break
                else:
                    plStand = True
                    break
        if plTotal == 21:
            plStand = True
        elif plTotal > 21:
            plTotal = changeAce(playerHand, plTotal)
            if plTotal > 21:
                winner = -1
                break
        print("Dealer's current hand is: ")
        print(dealerHand)
        if dlTotal < 17:
            card = drawCard(dealerHand)
            dlTotal = dlTotal + cardVal(card)
        else:
            dlStand = True
        if dlTotal == 21:
            dlStand = True
        elif dlTotal > 21:
            dlTotal = changeAce(dealerHand, dlTotal)
            if dlTotal > 21:
                winner = 1
                break
        if plStand == True and dlStand == True:
            break
    if winner == -1:
        print("BUST! The house wins!")
    elif winner == 1:
        print("BUST! The player wins!")
    else:
        if dlTotal > plTotal:
            print("The house wins!")
        elif plTotal > dlTotal:
            print("The player wins!")
        else:
            if len(playerHand) < len(dealerHand):
                print("The player wins!")
            elif len(playerHand) > len(dealerHand):
                print("The house wins!")
            else:
                print("It was a tie!")
    