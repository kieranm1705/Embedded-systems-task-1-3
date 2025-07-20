from word_guesser import SmartSolver

def run_trial(word):
    solver = SmartSolver()
    attempts = solver.guess(word)
    print(f"Solved '{word}' in {attempts} attempts.")
    return attempts

# Run multiple trials
if __name__ == "__main__":
    test_words = ["planet", "stream", "bottle", "pickle", "wrench", "button", "sprint", "garden"]
    total = 0
    for word in test_words:
        total += run_trial(word)
    avg = total / len(test_words)
    print(f"\n🔍 Average attempts: {avg:.2f}")
