'''
Rock crushes Scissors and crushes Lizard
Paper covers Rock and disproves Spock
Scissors cuts Paper and decapitates Lizard
Lizard eats Paper and poisons Spock
Spock smashes Scissors and vaporizes Rock

Our version of the game lets the user play against the computer. 
The game flow should go like this:

    The user makes a choice.
    The computer makes a choice.
    The winner is displayed.

Bonus: (Add context) OUTCOMES
    Rock crushes Scissors and crushes Lizard
    Paper covers Rock and disproves Spock
    Scissors cuts Paper and decapitates Lizard
    Lizard eats Paper and poisons Spock
    Spock smashes Scissors and vaporizes Rock
'''

# constants
# welcome prompt
# Get player input
# check validity
# get results (win, lose, tie)
# best of five?
# if the user types in a letter compare to the first letter  of word
# better to use s for scissors and sp for spock
# create a json file for the prompts

import random
import os

VALID_CHOICES = ['rock', 'paper', 'scissors', 'spock', 'lizard',
                 'r', 'p', 's', 'sp', 'l']
RULES = {
    'rock': ['scissors','lizard'],
    'paper': ['rock', 'spock'],
    'scissors': ['paper', 'lizard'],
    'lizard': ['paper', 'spock'],
    'spock': ['rock', 'scissors']
}

KEYS = list(RULES.keys())

OUTCOMES = {
        ('Rock', 'Scissors'): "Rock crushes Scissors",
        ('Rock', 'Lizard'): "Rock crushes Lizard",
        ('Paper', 'Rock'): "Paper covers Rock",
        ('Paper', 'Spock'): "Paper disproves Spock",
        ('Scissors', 'Paper'): "Scissors cuts Paper",
        ('Scissors', 'Lizard'): "Scissors decapitates Lizard",
        ('Lizard', 'Paper'): "Lizard eats Paper",
        ('Lizard', 'Spock'): "Lizard poisons Spock",
        ('Spock', 'Scissors'): "Spock smashes Scissors",
        ('Spock', 'Rock'): "Spock vaporizes Rock"
    }
def prompt(message):
    print(f'==> {message}')

def choice_check(choice):
    choice = choice.lower()
    while choice not in VALID_CHOICES:
        prompt("Hmm... that doesn't look like a valid choice.Try Again.\n")
        prompt(f'Choose one: {",".join(VALID_CHOICES[:5])}')
        prompt('You can use sp for spock and first letters for the rest.')
        choice = input().lower()
    return choice

prompt('Welcome to the Rock, Paper, Scissors, Lizard, Spock game!')
print()

def get_player_choice():
    prompt(f'Choose one: {",".join(VALID_CHOICES[:5])}')
    prompt('You can use sp for spock and first letters for the rest.')
    answer = input()
    answer = choice_check(answer)
    return answer

def choice_convert(answer):
    match answer:
        case 'rock' | 'r':
            answer = 'rock'
        case 'paper' | 'p':
            answer = 'paper'
        case 'scissors' | 's':
            answer = 'scissors'
        case 'lizard' | 'l':
            answer = 'lizard'
        case 'spock' | 'sp':
            answer = 'spock'
    return answer

### Bonus: (Add context)
def game_rules(player_input, computer_input):
    result = OUTCOMES[(player_input.capitalize(),
                       computer_input.capitalize())]
    prompt(result +'\n')

#player winning conditions
def player_outcome(player_choice, computer_choice):
    condition1 = (player_choice == KEYS[0]) and \
        (computer_choice in RULES[('rock')])

    condition2 = (player_choice == KEYS[1]) and \
        (computer_choice in RULES[('paper')])

    condition3 = (player_choice == KEYS[2]) and \
        (computer_choice in RULES[('scissors')])

    condition4 = (player_choice == KEYS[3]) and \
        (computer_choice in RULES[('lizard')])

    condition5 = (player_choice == KEYS[4]) and \
        (computer_choice in RULES[('spock')])
    return (condition1 or condition2 or condition3
        or condition4 or condition5)

# computer winning conditions
def computer_outcome(player_choice, computer_choice):
    condition_a = (computer_choice == KEYS[0]) and \
        (player_choice in RULES[('rock')])

    condition_b = (computer_choice == KEYS[1]) and \
        (player_choice in RULES[('paper')])

    condition_c = (computer_choice == KEYS[2]) and \
        (player_choice in RULES[('scissors')])

    condition_d = (computer_choice == KEYS[3]) and \
        (player_choice in RULES[('lizard')])

    condition_e = (computer_choice == KEYS[4]) and \
        (player_choice in RULES[('spock')])
    return (condition_a or condition_b or condition_c
          or condition_d or condition_e)

# best of five?
# get results (win, lose, tie)
def display_winner(player_choice, computer_choice,
                   players_score, computers_score):
    prompt(f'You chose {player_choice.capitalize()} and '
           f'Computer chose {computer_choice.capitalize()}.')
    if player_outcome(player_choice, computer_choice):
        players_score += 1
        game_rules(player_choice, computer_choice)
        prompt(f'The score is:\n'
               f'player:{players_score}\ncomputer:{computers_score}')
        print()
        if players_score == 5:
            prompt('You Win!')
    elif computer_outcome(player_choice, computer_choice):
        computers_score += 1
        game_rules(computer_choice, player_choice)
        prompt(f'The score is:\n'
               f'player:{players_score}\ncomputer:{computers_score}')
        print()
        if computers_score == 5:
            prompt('Computer Wins!')
    else:
        prompt("It's a tie!")
    return (players_score, computers_score)

# play another round?
def another_round():
    prompt('Would you like to play another game? (y/n)')
    choice = input().lower()
    return response_check(choice)


def response_check(choice):
    if choice not in ['y', 'yes', 'n', 'no']:
        prompt('Sorry, I did not get that. Try Again.')
        another_round()

    if choice in ['n', 'no']:
        prompt('Thank you for playing the game. BYE!')
        return False
    console_clear()
    return True


def console_clear():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def main():
    loop = True
    while loop:
        player_score = 0
        computer_score = 0
        # counter = 5
        while (player_score < 5) and (computer_score < 5):
            computer_choice = random.choice(VALID_CHOICES[:5])
            player_choice = get_player_choice()
            player_choice = choice_convert(player_choice)
            player_score, computer_score = (
                display_winner(player_choice, computer_choice,
                           player_score, computer_score))
            # print(player_score, computer_score)
            # counter -= 1
            # console_clear()
        loop = another_round()

main()