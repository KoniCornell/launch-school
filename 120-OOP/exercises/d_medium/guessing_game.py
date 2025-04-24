''' Number guesssing game '''
import random
import math

class GuessingGame:
    def __init__(self, low, high):
        self.low = low
        self.high = high
        

    def prompt(self):
        while True:
            guess = input(f'Enter a number between {self.low} and {self.high}: ')

            if not guess.isdigit():
                print('Invalid input. Please enter a number.')
                continue

            guess = int(guess)
            if self.low <= guess <= self.high:
                return guess

            print(f'Invalid guess. Number must be between {self.low} and {self.high}.')

    
    def compare(self, player, computer):
        if player < computer:
            print('Your guess is too low.')
            return False
        
        elif player > computer:
            print('Your guess is too high.')
            return False
        
        else:
            print("That's the number!")
            return True

    def play(self):
        number = random.randint(self.low, self.high)
        number_of_guesses = int(math.log2(self.high - self.low + 1)) + 1

        while number_of_guesses != 0:
            print(f'\nYou have {number_of_guesses} guesses remaining.')
            player_guess = self.prompt()
            decider = self.compare(player_guess, number)

            number_of_guesses -= 1
            if decider:
                print('\nYou won!')
                break

            elif number_of_guesses == 0:
                print(f'\nYou have no more guesses.' 
                      f'\nThe number was: {number}.You lost!')

            

game = GuessingGame(501, 1500)
game.play()
        
