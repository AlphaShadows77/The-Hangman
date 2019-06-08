from math import randrange


def get_random_word():
	with open("dictionary.txt", "r") as dictionary_file:
		words_number = dictionary_file.read(1) # There is the number of words in the file in the first line
		line = randrange(1, words_number)

		part_list_of_words = dictionary_file.readlines(words_number)
		word = part_list_of_words[line]
		return word
