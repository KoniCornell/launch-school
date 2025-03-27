'''
1. Initialize deck
2. Deal cards to player and dealer
3. Player turn: hit or stay
   - repeat until bust or stay
4. If player bust, dealer wins.
5. Dealer turn: hit or stay
   - repeat until total >= 17
6. If dealer busts, player wins.
7. Compare cards and declare winner.
'''
import random


# constants
BUST = 21
DECK_CARDS = ['2', '3', '4', '5', '6', '7', '8', '9','10',
    'Jack', 'Queen','King', 'Ace']
CARD_VALUES = {
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    '10': 10,
    'Jack': 10,
    'Queen': 10,
    'King': 10,
}
# 1. Initialize deck

def initialize_deck():
    deck = [card
            for card in DECK_CARDS
            for _ in range(4)]
    return deck

def shuffle(deck: list):
    random.shuffle(deck)
    # return deck

deck = initialize_deck()
shuffle(deck)
print(deck)
print()
print(len(deck))

# everything ace value
def get_ace_value(hand: list):
    total = sum([CARD_VALUES[key] 
                 for key in hand
                if key != 'Ace']) 
    
    if total < 21 and total + 11 <= 21:
            return 11
    else:
        return 1      

def update_ace_value(hand: list): 
    if 'Ace' in hand:
        hand.remove('Ace')
        card = get_ace_value(hand)
        hand.append(card)
    return hand
       

# 2. Deal cards to player and dealer

def deal_cards():
    player = [random.choice(deck) for _ in range(2)]
    for i in player:
        deck.remove(i)
    return player
 
# 3. Player turn: hit or stay
#  - repeat until bust or stay
def busted(cards: list):
    print(cards)
    print(sum_hand(cards))
    result = sum_hand(cards)
    return result > BUST

# update deck and hand after each hit
def update_hand(hand: list):
    card = random.choice(deck)
    deck.remove(card)
    if card == 'Ace':
        card = get_ace_value(hand)

    # card = get_ace_value(hand) if card == 'Ace' else card

    hand.append(card)

    return hand

# sum hand total
def sum_hand(lst: list):
    return sum([CARD_VALUES[key] if key not in (1, 11)
                                    else key
                                    for key in lst])


def player_turn(hand: list):
    # print(hand)
    # print(len(hand))
    hand = update_ace_value(hand)
    stay = False

    while not busted(hand):
        play_on = input('Hit or Stay?')
        if play_on == 'stay':
            break

        hand = update_hand(hand)

    if busted(hand):
        print('You lost. Dealer Wins!')
        # play again
        play_again()
    else:
        # print(hand)
        print('You chose to stay.')
        stay = True
    
    return [hand, stay]
        


# 5. Dealer turn: hit or stay
#    - repeat until total >= 17


def dealer_turn(hand: list):
    hand = update_ace_value(hand)
    
    result = sum_hand(hand)

    while result <= 17 and not busted(hand):
        hand = update_hand(hand)
        result = sum_hand(hand)

    # 6. If dealer busts, player wins.
    if busted(hand):
        print('Dealer lost. Player Wins!')
        play_again()

    return hand



def compare_cards(lst1: list, lst2: list):
    result_lst1 = sum_hand(lst1)
    result_lst2 = sum_hand(lst2)

    print(result_lst1)
    print(result_lst2)

    if result_lst1 == result_lst2:
        print("It's a tie!")
        
    elif result_lst1 < result_lst2:
        print('You lost. Dealer Wins!')
    else:
        print('You won')

# play again 
def play_again():
    print('\nPlay again? (y or n)')
    answer = input().lower()

    if answer not in ['y', 'yes']:
        print('Thanks for playing Twenty One')
        return False
    play_twenty_one()

# main loop

def play_twenty_one():
    loop = True
    while loop:
        # start
        deck = initialize_deck()
        shuffle(deck)

        # Deal
        player_cards = deal_cards()
        dealer_cards = deal_cards()

        print(f'Dealer has {dealer_cards[0]} and unknown card')
        print(f'You have: {player_cards[0]} and {player_cards[1]}')


        player_hand, stay = player_turn(player_cards)
        # Executes if player stays
        if stay:
            dealer_hand = dealer_turn(dealer_cards)

            # Compare
            print(player_hand, dealer_hand)
            compare_cards(player_hand, dealer_hand)
            loop = play_again()


play_twenty_one()
