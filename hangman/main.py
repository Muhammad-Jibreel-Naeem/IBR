import random
import nltk
from nltk.corpus import wordnet
import os

# nltk.download('wordnet', quiet=True)
# nltk.download('omw-1.4', quiet=True)


# Clear console screen
def clear_console():
	pass


# Load words from a file
def load_words(filename="words.txt"):
	if not os.path.exists(filename):
		print(f"❗ File '{filename}' not found. Please create it with one word per line.")
		return []
	with open(filename, "r") as f:
		return [line.strip().lower() for line in f if line.strip().isalpha()]


# Get hint using WordNet
def get_hint(word):
	synsets = wordnet.synsets(word)
	if synsets:
		return synsets[0].definition()
	else:
		return "No hint available."


# Display the word with underscores
def display_word(word, guessed_letters):
	return " ".join([letter if letter in guessed_letters else "_" for letter in word])


# Play one round
def play_game(word):
	guessed_letters = set()
	wrong_guesses = 0
	max_wrong = 10
	hint = get_hint(word)

	while wrong_guesses < max_wrong:

		print("🎮 Hangman Round")
		print(f"The word has {len(word)} letters.")
		print(f"💡 Hint: {hint}")
		print("Lives Remaining:", max_wrong - wrong_guesses)
		print("Word:", display_word(word, guessed_letters))
		print("Guessed:", " ".join(sorted(guessed_letters)))

		guess = input("🔤 Guess the letter: ").lower()

		if guess == "answer":
			print("📢 The word is:", word)
			break

		if not guess.isalpha() or len(guess) != 1:
			print("❌ Please enter a single valid letter.")
			input("Press Enter to continue...")
			continue

		if guess in guessed_letters:
			print("⚠️ You already guessed that letter.")
			input("Press Enter to continue...")
			continue

		guessed_letters.add(guess)

		if guess in word:
			if all(letter in guessed_letters for letter in word):
				clear_console()
				print("🎉 You guessed the word:", word)
				break
		else:
			wrong_guesses += 1

	if wrong_guesses == max_wrong:
		clear_console()
		print("💀 Game Over! The word was:", word)
	clear_console()


# Main loop for 5 rounds
if __name__ == "__main__":
	words = load_words()
	if not words:
		print("❌ No words to play with. Please check your words.txt.")
	else:
		rounds_played = 0
		max_rounds = 5

		while rounds_played < max_rounds:
			word = random.choice(words)
			hint = get_hint(word)
			if hint == "No hint available.":
				continue  # skip this word, pick another
			print(f"\n🌀 Starting Round {rounds_played + 1} of {max_rounds}")
			play_game(word)
			rounds_played += 1
			if rounds_played != 5:
				clear_console()
				input("\n⏭️ Press Enter to continue to the next round...")
		print("\n🏁 Game Over! Thanks for playing Hangman!")