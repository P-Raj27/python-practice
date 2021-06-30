  
from collections import defaultdict
def Anagrams(words):
    '''
    words: list of words
    return : list of group of anagram
    '''
    anag=defaultdict(list)
	  for ele in words:
		  k=tuple(sorted(ele))  # sorted the characters of the word and made it tuple --- this is our KEY
		  anag[k].append(ele)   # if elements of words list match KEY then we store the word as VALUES
	  return(list(anag.values()))
