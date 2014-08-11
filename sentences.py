
def break_sentence(sentence):
	"""Split the sentence into its constituent words"""
	"""Returns array"""
	words = sentence.split(' ')
	return words

def sort_words(sentence):
	"""Sort the words in the sentence"""
	return sorted(break_sentence(sentence))
	
def first_word(sentence):
	"""Get the first word from the sentence"""
	"""pop(0) - Get the first item from the array"""
	return 	break_sentence(sentence).pop(0)
	
def last_word(sentence):
	"""Get the last word from the sentence"""
	"""pop(-1) - get the last item in an array"""
	return break_sentence(sentence).pop(-1)