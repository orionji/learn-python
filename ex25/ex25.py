def break_words(stuff):
	"""This function will break up words for us"""
	words = stuff.split(' ')
	return words
def sort_words(words):
	"""Sorts the words."""
	return sorted(words)


def print_first_word(words):
	"""rint the first word after popping it off."""
	word = words.pop(0)
	print(word)

def print_last_word(words):
	"""Print the last woed after popping it off."""
	word = words.pop(0)
	print(word)

def