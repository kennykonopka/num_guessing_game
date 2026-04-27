#Number Guessing Game
#Features num guessing game with levels ranging from easy, to medium, to hard




class Game():

    def init(self, guesses = 10, diff = "easy"):
        self.guesses = guesses
        self.diff = self.set_difficulty(diff)

    
    def set_difficulty(self, diff):
        diff = diff.lower()

        diff_levels = {"easy": 100, "medium": 300, "hard" : 1000}

        return diff_levels[diff]
