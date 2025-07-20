import random
import time
import collections

# Load the word list
with open("wordList.txt", "r", encoding="utf-8") as f:
    WORD_LIST = [line.strip().lower() for line in f if len(line.strip()) == 6]

# Build frequency map
letter_counts = collections.Counter("".join(WORD_LIST))

def score_word(word):
    return sum(letter_counts[c] for c in set(word))  # Unique letters only

# Base Solver
class Solver:
    def __init__(self):
        self.wordList = WORD_LIST
        self.guesses = []

    def guess(self, target):
        self.guesses = []
        attempts = 0
        while True:
            guess = self.nextGuess()
            response = self.getFeedback(guess, target)
            self.guesses.append({'word': guess, 'response': response})
            attempts += 1
            if guess == target:
                return attempts

    def getFeedback(self, guess, target):
        result = []
        for i in range(6):
            if guess[i] == target[i]:
                result.append('+')
            elif guess[i] in target:
                result.append('*')
            else:
                result.append('-')
        return ''.join(result)

    def nextGuess(self):
        return random.choice(self.wordList)  # Should be overridden

# Frequency-based SmartSolver
class SmartSolver(Solver):
    def __init__(self):
        super().__init__()
        self.scoredWords = sorted(self.wordList, key=score_word, reverse=True)

    def nextGuess(self):
        if not self.guesses:
            return self.scoredWords[0]  # Best starting word

        candidates = []
        for word in self.scoredWords:
            if self.isWordValid(word):
                candidates.append(word)

        return candidates[0] if candidates else "planet"

    def isWordValid(self, word):
        for g in self.guesses:
            if not self.matchesFeedback(word, g['word'], g['response']):
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

# --------------------------
# Performance Test
# --------------------------
NUM_TRIALS = 100
total_attempts = 0
max_attempts = 0
failed = 0

start = time.time()
for i in range(NUM_TRIALS):
    target = random.choice(WORD_LIST)
    solver = SmartSolver()
    attempts = solver.guess(target)
    total_attempts += attempts
    max_attempts = max(max_attempts, attempts)
    if attempts > 10:
        failed += 1
        print(f"[{i+1}/{NUM_TRIALS}] Solved '{target}' in {attempts} attempts.")
end = time.time()

average_attempts = total_attempts / NUM_TRIALS
print("\n🔍 Performance Summary:")
print(f"→ Average attempts: {average_attempts:.2f}")
print(f"→ Max attempts in any trial: {max_attempts}")
print(f"→ Failed guesses (>10 attempts): {failed}")
print(f"→ Time taken: {end - start:.2f} seconds")
