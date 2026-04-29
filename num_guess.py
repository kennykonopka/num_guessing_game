#Number Guessing Game
#Features num guessing game with levels ranging from easy, to medium, to hard
import random

class Game():

    def __init__(self, board):
        self.board = board
        self.max_guesses = None
        self.guesses = 0
        self.low = 1
        self.high = 0
        self.difficulty = None
        self.prev_guesses = []

    def play(self):
        #First, determine difficulty
        print("Welcome!, To begin, select a difficulty: easy, medium, or hard")
        string = False
        while not string:
            diff = (input("Enter difficulty:")).lower()

            if diff in ["easy", "medium", "hard"]:
                self.difficulty = diff
                string = True
            else:
                print("Please input a valid difficulty: easy, medium, or hard")

        self.max_guesses = self.set_difficulty(diff)[1]
        self.high = self.set_difficulty(diff)[0]

        #Determine random number
        self.num = random.randint(self.low, self.high)

        #While loop to check guesses
        while self.guesses < self.max_guesses:
            guess = self.get_guess()
            self.guesses += 1
            self.prev_guesses.append(guess)

            #Winner logic
            result = self.check_guess(guess)
            if result == "exact":
                print(f"Guesses: {self.prev_guesses}\nYou won in {self.guesses} attempts!")
                name = input("Enter your name: ")
                self.board.add(name, self.guesses,self.difficulty)
                self.board.display(self.difficulty)
                self.play_again()
                return
            #Check high/low
            elif result == "less":
                print(f"Your guess of {guess} is too low.")
            elif result == "greater":
                print(f"Your guess of {guess} is too high.")
        
        #Loser logic
        print(f"Guesses: {self.prev_guesses} \nYou ran out of guesses! You lose! The number was: {self.num}")
        self.play_again()

    #Function to receive guess input
    def get_guess(self):
        print(f"Number or guesses: {self.guesses}")
        while True:
            try:
                guess = int(input(f"Enter a number ({self.low}-{self.high}): "))
                return guess
            except ValueError:
                print("Invalid input. Try again. \n")

    #Function to check guess    
    def check_guess(self, guess):
        if guess == self.num:
            return "exact"
        elif guess < self.num:
            return "less"
        elif guess > self.num:
            return "greater"

    #Function to set difficulty
    def set_difficulty(self, diff):
        diff = diff.lower()

        diff_levels = {"easy": [100, 10], "medium": [300, 12], "hard" : [1000,15]}

        return diff_levels[diff]
    
    def play_again(self):
        while True:
            again = input("Play again? Yes or no \n")
            again = again.lower()
            if again == "yes":
                new_game = Game(self.board)
                new_game.play()
                return
            elif again == "no":
                return
            else:
                print("Invalid input. Please type yes or no")

class Leaderboard():

    def __init__(self):
        self.leaders = {
            "easy": {},
            "medium": {},
            "hard": {}
        }
    
    #adds scores
    def add(self, name, guesses, difficulty):

        board = self.leaders[difficulty]

        #keeps only best score
        if name in board:
            if guesses < board[name]:
                board[name] = guesses
        else:
            board[name] = guesses

    #display leaderboard
    def display(self, difficulty):

        print(f"\n{difficulty} leaderboard:")

        #sorts by lowest number of guesses
        board = sorted(self.leaders[difficulty].items(), key=lambda x: x[1])

        #shows top 3 on leaderboard
        for name, guesses in board[:3]:
            print(f"{name}: {guesses} guesses")

        print("\n")

if __name__ == "__main__":
    board = Leaderboard()
    game = Game(board)
    game.play()
    
#FINAL PRODUCT