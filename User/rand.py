#!/usr/bin/python

import heapq
import random

def isValid(word):
    return (len(word) < 7 and word.isalpha())

def genPass(length):
	lines       = (line for line in open("/usr/share/dict/american-english"))
	words       = (line.strip() for line in lines)
	valid_words = (word for word in words if isValid(word))
	word_pairs  = ((random.random(), word) for word in valid_words)
	rand_pairs  = heapq.nlargest(2, word_pairs)

	rand_words  = [word for rand, word in rand_pairs]
	password = (rand_words[0] + "_" + rand_words[1]).lower()

	return password
