import random


def generate_code():
	digits = list("0123456789")
	random.shuffle(digits)
	return digits[:3]


def get_clues(code, guess):
	if guess == code:
		return ["🎉 Correct!"]

	clues = []
	for i in range(3):
		if guess[i] == code[i]:
			clues.append("✅")
		elif guess[i] in code:
			clues.append("🔁")
		else:
			clues.append("❌")
	return clues


def is_valid_guess(guess):
	return guess.isdigit() and len(guess) == 3 and len(set(guess)) == 3


def play_game():
	code = generate_code()
	attempts = 10
	print("🧠 Guess the 3-digit secret code. All digits are unique.")
	print("Hints: ✅ = Correct Place | 🔁 = Wrong Place | ❌ = Not in Code")

	while attempts > 0:
		guess_input = input(f"\n🔢 Enter guess ({attempts} tries left): ")
		if not is_valid_guess(guess_input):
			print("❌ Invalid input. Use 3 unique digits.")
			continue

		guess = list(guess_input)
		clues = get_clues(code, guess)

		print("💡 Clues:", " ".join(clues))

		if guess == code:
			break

		attempts -= 1

	if attempts == 0 and guess != code:
		print("💀 Out of tries! The code was:", "".join(code))
	print("🏁 Game Over.")


if __name__ == "__main__":
	play_game()