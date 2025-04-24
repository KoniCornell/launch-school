''' OOP Rock Paper Scissors'''

import random

class Player:
    '''Player class '''
    CHOICES = ('rock', 'paper', 'scissors')

    def __init__(self):
        self.move = None

class Human(Player):
    ''' Human class '''
    def __init__(self):
        super().__init__()

    def choose(self):
        ''' player move choice '''
        prompt = 'Please choose rock, paper, or scissors: '

        while True:
            choice = input(prompt).lower()
            if choice.lower() in Player.CHOICES:
                break

            print(f'Sorry, {choice} is not valid')

        self.move = choice

class Computer(Player):
    ''' Computer class '''
    def __init__(self):
        super().__init__()

    def choose(self):
        ''' computer move choice '''
        self.move = random.choice(Player.CHOICES)

class RPSGame:
    ''' RPSGame class '''
    def __init__(self):
        self._human = Human()
        self._computer = Computer()

    def _display_welcome_message(self):
        print('Welcome to Rock Paper Scissors!')

    def _display_goodbye_message(self):
        print('Thanks for playin Rock Paper Scissors. Goodbye!')

    def _human_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((human_move == 'rock' and computer_move == 'scissors') or
                (human_move == 'paper' and computer_move == 'rock') or
                (human_move == 'scissors' and computer_move == 'paper'))

    def _computer_wins(self):
        human_move = self._human.move
        computer_move = self._computer.move

        return ((computer_move == 'rock' and human_move == 'scissors') or
                (computer_move == 'paper' and human_move == 'rock') or
                (computer_move == 'scissors' and human_move == 'paper'))

    def _display_winner(self):
        print(f'You chose: {self._human.move}')
        print(f'The computer chose: {self._computer.move}')

        if self._human_wins():
            print('You win!')
        elif self._computer_wins():
            print('Computer wins!')
        else:
            print("It's a tie")

    def _play_again(self):
        answer = input('Would you like to play again? (y/n)')
        return answer.lower().startswith('y')

    def play(self):
        ''' Main game loop '''
        self._display_welcome_message()

        while True:
            self._human.choose()
            self._computer.choose()
            self._display_winner()

            if not self._play_again():
                break
        self._display_goodbye_message()


game = RPSGame()
game.play()
