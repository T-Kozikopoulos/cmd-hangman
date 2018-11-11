import json
from random import choice


# Check if the letter guessed is in the word.
def find(lst, a):
    result = []
    for i, j in enumerate(lst):
        if j == a:
            result.append(i)
    return result


# Load the word data.
with open('words.json') as f:
    words = json.load(f)

# Pick a random word.
word = choice(words)

# Declare score variables.
count = 0
chances = 4

# Split the word into letters.
letters = list(word)
word_list = []

# Add word letters to a separate list.
for l in letters:
    word_list.append('-')

# Let the games begin!
print('Welcome to Hangman \n\n Try to guess the {} letter word. \n'.format(str(len(letters))))
print(' '.join(word_list) + '\n\n')

# Keeping score, plus the main part of the game.
while count <= chances:
    chances_left = chances - count
    letter = input("Enter a letter: ")

	# Check if the guess was right or wrong.
	if letter in letters:
        indexes = find(letters, letter)
        for i in indexes:
            word_list[i] = letter
        print('\n' + ' '.join(word_list) + '\n' + 'Good guess! \n')
    else:
        count += 1
        print('Wrong, try again!')
        print('{} chances left. \n'.format(str(chances_left)))

    combined = ''.join(word_list)

	# Establish the game ending conditions.
    if combined == word:
        print('You win! The word was: {}.'.format(word))
        break

    if count > chances:
        print('Game over. The word was: {}.'.format(word))
        break
