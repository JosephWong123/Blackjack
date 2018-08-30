import sys
import random
# from PyQt4 import QtGui

# TODO: split

class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit  # needed when UI is developed


class Hand:
    def __init__(self, id, cards, points=0):
        self.id = id
        self.cards = cards
        self.points = points

    def score(self):
        value = 0
        numAces = 0
        for x in self.cards:
            value += numValue.get(x.value)
            if x.value == 'A':
                numAces += 1
        # print(numAces)
        while value > 21 and numAces > 0:
            value -= 10
            numAces -= 1
        self.points = value
        return value

count = 0.0
suits = ['heart', 'diamond','club','spade']
values = ['A', '2', '3', '4', '5', '6', '7', '8', '9','10', 'J', 'Q', 'K']
numValue = { # maps each card to a numerical value
    'A': 11,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'J': 10,
    'Q': 10,
    'K': 10
}
deck = []
playerHand = []# length of 2 initially , type card
compHand = [] # length of 2 initially
startDecks = 0
playAgain = True
split = False
handList = []
last = len(handList)-1  #last value in handList

def createDeck(numDecks):
    global startDecks
    startDecks = numDecks
    for x in range(numDecks):
        for suit in suits:
            for value in values:
                deck.append(Card(value, suit))


def deal():
    global deck
    for y in handList:
        for x in range(2):
            randInt = random.randint(0,len(deck)-1)
            if y.id != 99:
                y.cards.append(deck[randInt])
                deck.pop(randInt)
        # playerHand.append(deck[randInt])
        # deck.pop(randInt)
        # print("length:" + str(len(deck)))
    i = random.randint(0, len(deck))
    handList[last].cards.append(deck[i])
    deck.pop(i)


def updateCount():
    for x in handList:
        for y in x.cards:
            score(numValue.get(y.value))
    for x in handList[last].cards:
        score(numValue.get(x.value))


def score(val):
    global count
    if val <= 6 or val == 11:
        count += 1 / startDecks
    elif val == 10:
        count -= 1 / startDecks


def hit(hand): # hand = listHand[x].cards
    global deck
    i = random.randint(0, len(deck)-1)
    hand.append(deck[i])
    print("Dealt a " + deck[i].value)
    deck.pop(i)
    return hand

# def split(hand):
#    if hand[0].value != hand[1].value:
#        return
#    else:
#        global split
#        split = True
#        hand.pop(1)
#        splitHand = [hand[0]]
#        splitHand = hit(splitHand)
#        hand = hit(hand)



def reveal():
    i = random.randint(0, len(deck)-1)
    handList[len(handList) - 1].cards.append(deck[i])
    deck.pop(i)

def showCount():
    print(count)

#def getHandValue(hand):
#   value = 0
#    numAces = 0
 #   for x in hand:
#        value += numValue.get(x.value)
#        if x.value == 'A':
#            numAces += 1
#    # print(numAces)
 #   while value > 21 and numAces > 0:
#        value -= 10
#        numAces -= 1
#    return value


def computerTurn():
    global handList
    value = handList[last].score()
    while value < 17:
        handList[last].cards = hit(handList[last].cards)
        value = handList[last].score()

decks = int(input("How many decks would you like?"))
createDeck(decks)

while playAgain:
    players = int(input("How many people are playing?"))
    for x in range(players):
        handList.append(Hand(id=x+1, cards=[]))
    handList.append(Hand(id=99, cards=[]))  # 99 = computer
    rev = input("Reveal the current running count?")
    if rev.lower() == 'yes':
        print(count)
    deal()
    for x in handList:
        if x.id != 99:
            print("Player " + str(x.id) + "'s cards are: " + x.cards[0].value + " and " + x.cards[1].value + "\n")
    print("The computer has: " + handList[last].cards[0].value + " and a hidden card.")
    for x in handList:
        if x.id != 99:
            playerScore = x.score()
            while playerScore <= 21:
                option = input("Player " + str(x.id) + " Would you like to hit or stand?")
                if option.lower() == 'hit':
                    x.cards = hit(x.cards)
                    playerScore = x.score()

                elif option.lower() == 'stand':
                    break
                elif option.lower() == 'split':
                    split(x)
            print("Your score is " + str(playerScore))
    reveal()
    print("The computer's hand after revealing the hidden card is: " + handList[last].cards[0].value + " " + handList[last].cards[1].value)
    computerTurn()
    compScore = handList[last].score()
    print("The computer's score is " + str(compScore))
    for x in handList:
        if x.id != 99:
            if x.points > 21:
                print("Player " + str(x.id) + " loses! (Bust)")
            elif compScore > 21:
                print("All players win!")
                break
            else:
                if x.points > compScore:
                    print("Player " + str(x.id) + " wins!")
                elif x.points == compScore:
                    print("Player " + str(x.id) + " draws.")
                else:
                    print("Player " + str(x.id) + " loses.")
    updateCount()
    replay = input("Play again? (yes/no)")
#    playerHand = []
#    compHand = []
    handList = []
    if replay.lower() == 'no':
        playAgain = False
    if len(deck) < 10:
        print("Thank you for playing!")
        break


