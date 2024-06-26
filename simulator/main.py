import random


def generate_deck():

    suits = ["D", "C", "H", "S"]
    ranks = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    deck = []

    for i in ranks:
        for j in suits:
            deck.append([i, j])

    random.shuffle(deck)

    return deck


def deal(deck, number_of_cards):

    dealt_cards = []

    for i in range(number_of_cards):
        dealt_cards.append(deck[-1])
        deck.pop(-1)

    return dealt_cards


def calculate_hand(hand):

    card_values = {
        "J": 10,
        "Q": 10,
        "K": 10,
        "A": [1, 11]
    }

    hand_value = 0

# Appends all aces to the end of list 

    temp_hand = hand.copy()

    for card in temp_hand:
        if card[0] == "A":
            hand.append(hand.pop(hand.index(card)))

    for card in hand:
        if card[0] in card_values:

            if card[0] == "A":
                if hand_value > 10:
                    hand_value += card_values["A"][0]
                else:
                    hand_value += card_values["A"][1]
            else:
                hand_value += card_values[card[0]]

        else:
            hand_value += int(card[0])

    return hand_value

# Checks if hand is soft 17

def is_soft17(hand):
    if calculate_hand(hand) == 17:

        for i in range(len(hand)):
            if hand[i][0] == "A":
                hand[i][0] = "1"
        
        if calculate_hand(hand) == 7:
            return True
        else:
            return False
     
    else:
        return False


def game():

    deck = generate_deck()
    player_hand = deal(deck, 2)
    dealer_hand = deal(deck, 2)
    player_value = calculate_hand(player_hand)
    dealer_value = calculate_hand(dealer_hand)

    player_bust = False
    dealer_bust = False
    player_21 = False
    dealer_21 = False

    if player_value == 21:
        player_21 = True
    if dealer_21 == 21:
        dealer_21 = True

# Player Sequence

    print(f"Your Hand: {player_hand}")
    print(f"Dealer's First Card: {dealer_hand[0]}")

    while not player_bust and not player_21:

        player_move = input("Type 'H' to hit, Type 'S' to stand: ").upper()
        print()

        if player_move == "H":

            player_hand += deal(deck, 1)
            player_value = calculate_hand(player_hand)
            print(f"Your Hand: {player_hand}")

        else:
            break

        if player_value > 21:
            player_bust = True
            print("PLAYER BUST")
        elif player_value == 21:
            player_21 = True

    print(f"Dealer's Hand: {dealer_hand}")  

# Dealer Sequence

    while not dealer_bust and not player_bust and not dealer_21:

        if dealer_value > 21:
            dealer_bust = True
            print("DEALER BUST")
        
        elif dealer_value == 21:
            dealer_21 = True

        elif dealer_value < 17 or is_soft17(dealer_hand):
            dealer_hand += deal(deck, 1)
            dealer_value = calculate_hand(dealer_hand)
            print(f"Dealer's Hand: {dealer_hand}")

        else:
            break

# Win Conditions

    if player_bust == False and dealer_bust == False:

        if player_value < 21:
            player_difference = 21 - player_value
        else:
            player_difference = player_value % 21

        if dealer_value < 21:
            dealer_difference = 21 - dealer_value
        else:
            dealer_difference = dealer_value % 21

        if player_value == dealer_value:
            print("PUSH")
        elif player_difference < dealer_difference:
            print("YOU WIN")
        else:
            print("DEALER WINS")

game()
