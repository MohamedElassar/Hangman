# Hangman Game
#Author: Mohamed Elassar. Contact me: mohamedelassar1997@gmail.com
#Year: 2020
#Please read the associated ReadMe file to learn how to run this game. Enjoy :)
import random
import string

WORDLIST_FILENAME = "words.txt"

#Function to load a list of words into the program. The secret word will be selected randomly from this list
#Please make sure you download the file "words.txt" alongside this file
def load_words():
    print("Loading word list from file...")
    inFile = open(WORDLIST_FILENAME, 'r')
    line = inFile.readline()
    wordlist = line.split()
    print("  ", len(wordlist), "words loaded.")
    return wordlist

#Function to choose a word randomly from the list of words imported from words.txt. I generate a random number between 0 and the length of the 
#list of words. Then pick the word at that random index
def choose_word(list_of_words):
	x = len(list_of_words) - 1
	y = random.randint(0, x)
	return list_of_words[y]

#To keep track of the user stats, I use a dictionary with the following variables: num_attempts, num_errors, available_letters (available to guess from), 
#and temp_sol (the solution that the player has so far). This function initializes this dictionary
def initialize_stats(stats, length_of_word):
	stats["num_attempts"] = int(1.2*length_of_word)
	stats["num_errors"] = 0
	stats["available_letters"] = "abcdefghijklmnopqrstuvwxyz"
	stats["temp_sol"] = "-"*length_of_word

#Function to print all the stats after every round
def print_stats(stats):
	print("What we have so far: " + stats["temp_sol"])
	print("Attempts Left: " + str(stats["num_attempts"]))
	print("Available Letters: " + stats["available_letters"])

#Function that processes the user's guess. First it checks if the letter inputter is a lowercase alphabetical character. Then, it checks
#if the letter is in the list of available letters to guess from. If it is, the program then removes that letter from the list of pickable letters and proceeds to process
#the letter: if the letter is NOT in the secret word, the number of attempts left is reduced by 1. Otherwise, the user's temporary solution is updated and every instance
#of the guessed letter is shown
def process_input(inp, stats, secret_word, length_of_word):
	if(inp not in string.ascii_lowercase):
		print("Error! Please enter a lowercase alphabetical character")
	elif(inp not in stats["available_letters"]):
		print("Error! You already guessed this letter. Please try again")
	else:
		stats["available_letters"] = stats["available_letters"].replace(inp, "")
		if(inp not in secret_word):
			print("Whoops! The letter you guessed is not in the secret word :(")
			stats["num_errors"] = stats["num_errors"]  + 1
			stats["num_attempts"] = stats["num_attempts"]  - 1
		else:
			print("Nice! The letter you guessed is indeed in the secret word!")
			for i in range(length_of_word):
				if(inp == secret_word[i]):
					stats["temp_sol"] = stats["temp_sol"][:i] + inp + stats["temp_sol"][i+1:]
			if(stats["temp_sol"] == secret_word):
				stats["isGuessed"] = True

#Main hangman function. It keeps running as long as the user's number of attempts left is > 0 and he hasn't guessed the full word yet
def hangman():
	list_of_words = load_words()
	secret_word = choose_word(list_of_words)
	length_of_word = len(secret_word)

	stats = {"num_attempts":None, "num_errors":None, "available_letters":None, "temp_sol":None, "isGuessed":False}
	initialize_stats(stats, length_of_word)

	print("I am thinking of a " + str(length_of_word) + " letter word. Let's begin!")

	while(stats["num_attempts"] > 0 and not stats["isGuessed"]):

		print("****************************************************")

		print_stats(stats)
		inp = input("Please enter a letter: ")
		process_input(inp, stats, secret_word, length_of_word)

	if(stats["isGuessed"]):
		print("Congratulations! You Won! The word was "  + secret_word)
	else:
		print("Sorry :( The correct word is " + secret_word)

if __name__ == "__main__":
    hangman()
