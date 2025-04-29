import nltk, os, random;
from code_guess import play_game
from nltk.corpus import wordnet;


def load_words(filename='words.txt'):
	if not os.path.isfile(filename):
		print("That file doesn't exist. ❌❎");
	else:
		with open(filename, 'r') as f:
			return [line.strip().lower() for line in f];

def get_definition(word):
	synset = wordnet.synsets(word);
	clue = synset[0].definition() if synset else False;
	return clue;

score = 0

def play_game(words):

	while True:
		word = random.choice(words);
		clue = get_definition(word);


		if not clue:
			continue;
		break;
	print(f'Clue: {clue} 🧩 \n');
	print(f'Length of word: {len(word)} 📏\n')
	global score;
	guess = input('Guess the word: ');

	if guess.lower() == word.lower():
		score+=1;
		print(f'Correct! Your score is: {score} \n');
	elif guess.lower() == 'q':
		exit()
	elif guess.lower() == 'answer':
		print(f'The word was: {word} \n')
	else:
		print(f'Incorrect! The word was: {word} \n');



if __name__ == '__main__':
	print("Welcome to my Synonym Riddle! 🎮 ('q' to quit). \n");
	while True:
		words = load_words()
		play_game(words)
	score = 0;

	print('Your score is:', score)
