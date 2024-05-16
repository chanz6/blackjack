import random

# generates deck 

def generate_deck():

    suits = ["D", "C", "H", "S"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    cards = []

    for i in suits:
        for j in ranks:
            cards.append([i,j])

    return cards

# shuffle deck

def shuffle_deck(deck):

    random.shuffle(deck)

# deal card(s)

def deal(deck, number_of_cards):

    cards = []
    
    for i in range(number_of_cards):
        cards.append(deck[len(deck) - 1])
        deck.pop(len(deck) - 1)

    return cards
    
# calculate hand value

def hand_value(hand):

    value = 0
    
    for card in hand:

        rank = card[1]
    
        match rank:

            case "2":
                value += 2

            case "3":
                value += 3

            case "4":
                value += 4
            
            case "5":
                value += 5

            case "6":
                value += 6

            case "7":
                value += 7

            case "8":
                value += 8

            case "9":
                value += 9

            case "10":
                value += 10

            case "J":
                value += 10
            
            case "Q":
                value += 10
            
            case "K":
                value += 10

            case "A":
                if value <= 10:
                    value += 11
                else:
                    value += 1
        
            case _:
                value += 0

    return value

# test(multi-line comment out)   

"""
deck = generate_deck()
shuffle_deck(deck)

player_hand = []

delt_cards = deal(deck, 2)

for i in range(len(delt_cards)):
    player_hand.append(delt_cards[i])

print(player_hand)
print()
print()
print(hand_value(player_hand))
"""

