from solver import Solver

class SmartSolver(Solver):
    def __init__(self):
        super().__init__()

    def nextGuess(self):
        if not self.guesses:
            return "planet"  # fixed good starter

        filtered_words = [word for word in self.wordList if self.isWordValid(word)]
        return filtered_words[0] if filtered_words else "planet"

    def isWordValid(self, word):
        for guess in self.guesses:
            if not self.matchesFeedback(word, guess['word'], guess['response']):
                return False
        return True

    def matchesFeedback(self, candidate, guess, feedback):
        for i in range(6):
            if feedback[i] == '+':
                if candidate[i] != guess[i]:
                    return False
            elif feedback[i] == '*':
                if guess[i] not in candidate or candidate[i] == guess[i]:
                    return False
            elif feedback[i] == '-':
                if guess[i] in candidate:
                    return False
        return True
