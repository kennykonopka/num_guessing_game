#Number Guessing Game
#Features num guessing game with levels ranging from easy, to medium, to hard
import random

class Game():

    def init(self, diff = "easy"):
        self.max_guesses = None
        self.guesses = 0
        self.low = 1
        self.high = 0

    def play(self):
        print("Welcome!, To begin, select a difficulty: easy, medium, or hard")
        string = False
        while not string:
            diff = (input("Enter difficulty:"))
            if isinstance(diff,str):
                diff = diff.lower()
            else:
                "Please input a valid difficulty: easy, medium, or hard"
            if diff is "easy" or "medium" or "hard":
                string = True

        self.max_guesses = self.set_difficulty(diff)[1]
        self.high = self.set_difficulty(diff)[0]

        self.num = random.randint(self.low, self.high)

        while self.guesses < self.max_guesses:
            guess = self.get_guess()
            self.guesses += 1

            if self.check_guess(guess):
                print(f"You won in {self.guesses} attempts!")
                return


    def get_guess(self):
        while True:
            try:
                guess = int(input(f"Enter a number ({self.low}-{self.high}): "))
                return guess
            except ValueError:
                print("Invalid input. Try again.")

    def check_guess(self, guess)
        if guess == self.num:
            return True
        return False

    def set_difficulty(self, diff):
        diff = diff.lower()

        diff_levels = {"easy": [100, 10], "medium": [300, 15], "hard" : [1000,20]}

        return diff_levels[diff]
