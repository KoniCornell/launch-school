'''
Building a game of tic tac toe
    1. Display the initial empty 3x3 board.
    2. Ask the user to mark a square.
    3. Computer marks a square.
    4. Display the updated board state.
    5. If it's a winning board, display the winner.
    6. If the board is full, display tie.
    7. If neither player won and the board is not full, go to #2
    8. Play again?
    9. If yes, go to #1
    10. Goodbye!
'''

import random
import os

# Constants
INITIAL_MARKER = ' '
HUMAN_MARKER = 'X'
COMPUTER_MARKER = 'O'

# Display an empty board
def prompt(message):
    print(f'==> {message}')

def welcome():
    print('*' * 30)
    prompt(' Welcome to TicTacToe. <==')
    prompt('     Best of 5 game    <==')
    print('*' * 30)

welcome()

def display_board(board):
    

    prompt(f"You are {HUMAN_MARKER}. Computer is {COMPUTER_MARKER}.")

    print('')
    print('     |     |')
    print(f"  {board[1]}  |  {board[2]}  |  {board[3]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[4]}  |  {board[5]}  |  {board[6]}")
    print('     |     |')
    print('-----+-----+-----')
    print('     |     |')
    print(f"  {board[7]}  |  {board[8]}  |  {board[9]}")
    print('     |     |')
    print('')

def clear_screen():
    # For Windows
    if os.name == 'nt':
        _ = os.system('cls')
    # For macOS and Linux
    else:
        _ = os.system('clear')



def initialize_board():
    return {square: INITIAL_MARKER for square in range(1,10)}


# board = initialize_board()
# display_board(board)

# 2. Ask the user to mark a square.



def empty_squares(board):
    return [key 
            for key, value in board.items() 
            if value == INITIAL_MARKER]


def join_or(lst: list, delimiter: str = ', ', last: str = 'or'):
    lst = [str(char) for char in lst]
    last = f'{last} '

    if len(lst) < 1:
        return ''
    
    elif len(lst) == 1:
        return str(*lst)
    
    elif len(lst) == 2:
        return (' '+last).join(lst)
    else:
        string = delimiter.join(lst)
        return ''.join([string[:-1], last, str(string[-1])])

def player_chooses_square(board):

    while True:
        valid_choices = [str(num) for num in empty_squares(board)]
        prompt(f'Choose a square {join_or(valid_choices)}:')
        square = input()

        if square in valid_choices:
            break
        
        prompt('Sorry, that is not a valid choice.')

    board[int(square)] = HUMAN_MARKER

# 3. Computer marks a square.

def computer_chooses_square(board):
    if len(empty_squares(board)) == 0:
        return
    # winning_lines = [
    #     [1, 2, 3], [4, 5, 6], [7, 8, 9],
    #     [1, 4, 7], [2, 5, 8], [3, 6, 9],
    #     [1, 5, 9], [3, 5, 7]
    # ]
    # for line in winning_lines:
    #     sq1, sq2, sq3 = line
    #     if (board[sq1], board[sq2]) == (HUMAN_MARKER, HUMAN_MARKER):
    #         square = sq3
    #         board[square] = COMPUTER_MARKER
    #         return

    square = random.choice(empty_squares(board))
    board[square] = COMPUTER_MARKER

# check winner or tie
def someone_won(board):
    return bool(detect_winner(board))

def board_full(board):
    return len(empty_squares(board)) == 0

def detect_winner(board):
    winning_lines = [
        [1, 2, 3], [4, 5, 6], [7, 8, 9],
        [1, 4, 7], [2, 5, 8], [3, 6, 9],
        [1, 5, 9], [3, 5, 7]
    ]

    for line in winning_lines:
        sq1, sq2, sq3 = line
        checker = {board[sq1], board[sq2], board[sq3]}

        if checker == {HUMAN_MARKER}:
            return 'Player'
        elif checker == {COMPUTER_MARKER}:
            return 'Computer'
        
    return None

# score
def display_winner(players: dict):
    print()
    prompt('Game Over')
    print()
    if players['player'] > players['computer']:
        prompt('player won!')
        prompt(f'player: {players['player']}')
        prompt(f'computer: {players['computer']}')
    
    elif players['player'] < players['computer']:
        prompt('player won!')
        prompt(f'player: {players['player']}')
        prompt(f'computer: {players['computer']}')
    
    else:
        prompt("It's a tie.")
    
    return

def display_scores(player_scores: dict):
    prompt(f'player: {player_scores['player']}')
    prompt(f'computer: {player_scores['computer']}')

# play again 
def play_again():
    prompt('Play again? (y or n)')
    answer = input().lower()

    if answer not in ['y', 'yes']:
        prompt('Thanks for playing TicTacToe')
        return 
    
    play_tic_tac_toe()


# main loop

def play_tic_tac_toe():
    scores = {
        'player': 0,
        'computer': 0
        }
    games = 0
    while games < 5:
        board = initialize_board()
        prompt('The scores are: ')
        display_scores(scores)
        print()

        while True:
            display_board(board)
            
            player_chooses_square(board)
            if someone_won(board) or board_full(board):
                scores['player'] += 1
                break

            computer_chooses_square(board)
            if someone_won(board) or board_full(board):
                scores['computer'] += 1
                break

        display_board(board)

        # winner or tie
        if someone_won(board):
            prompt(f'{detect_winner(board)} won this round!')
        else:
            prompt("It's a tie.")
        games += 1

    # display winner
    display_winner(scores)

    # play again
    play_again()



play_tic_tac_toe()
