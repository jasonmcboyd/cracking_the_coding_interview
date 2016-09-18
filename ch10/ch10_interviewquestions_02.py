# 10.2 Group Anagrams: Write a method to sort an array of strings so that all
# the anagrams are next to each other.
def groupAnagrams(words, inPlace=False):
	# If we are not sorting in place then copy 'words' to a new list.
	if inPlace == False:
		words = words[:]
		
	# Map each word to a key that can be used to sort the words.  In this case
	# the key is just the word with the letters in alphabetical order.  Words
	# with the same key are anagrams of each other.
	words.sort(key = lambda word: (''.join(sorted(word)), word))
	
	return words