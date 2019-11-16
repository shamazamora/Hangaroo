# -*- coding: utf-8 -*-
def Hangaroo(secretWord):
    print('Welcome to Hangaroo!')
    print('The word I want you to guess is', len(secretWord), "letters long.")
    mistakesMade = 0
    lettersGuessed = []
    while 8 - mistakesMade > 0:
        if isWordGuessed(secretWord, lettersGuessed) == True:
            print('--------')
            print('You guessed right!')
            break
        else:
        	print('--------')
        	print('You have', 8 - mistakesMade, 'guesses left.')
        	print('Available letters:', getAvailableLetters(lettersGuessed))
        	guess = str(input('Guess a letter:')).lower()
        	if guess in secretWord and guess not in lettersGuessed:
        		lettersGuessed.append(guess)
        		print('You got one right! :', getGuessedWord(secretWord, lettersGuessed))
        	elif guess in lettersGuessed:
        		print("Letter is repeated: ", getGuessedWord(secretWord, lettersGuessed))
        	elif guess not in secretWord:
        		print("You guessed the wrong letter :", getGuessedWord(secretWord, lettersGuessed))
        		lettersGuessed.append(guess)
        		mistakesMade += 1
        if 8 - mistakesMade == 0:
        	print('--------')
        	print('You used up all your guesses. The word was', secretWord)
        	break
        else:
        	continue