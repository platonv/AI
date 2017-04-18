#!/usr/bin/python3

from random import randint
from functools import *
import statistics

N = 20
vowels = ['a', 'e', 'i', 'o', 'u']
sampleSize = 10
whiteRequirement = 5
taggedWithVowel = 1
testCases = 50

def color(n):
	if n == 0:
		return 'white'
	else:
		return 'blue'

class Ball:
	def __init__(self):
		self.color = color(randint(0, 1))
		self.letter = chr(ord('a') + randint(0, 26))

	def __str__(self):
		return '(' + self.color + ' ' + self.letter + ')'

	def __repr__(self):
		return str(self)

def generateSolution(n):
	balls = [Ball() for x in range(n)]
	return balls

def error(x):
	result = 0
	if x.color == 'white':
		result += 1
	if x.letter in vowels:
		result += 1
	return result

def fitness(solution, sampleSize, whiteRequirement, taggedWithVowel):
	return sum(error(x) for x in solution[:sampleSize])

if __name__ == '__main__':
	results = []
	for t in range(testCases):
		result = fitness(generateSolution(N), sampleSize, whiteRequirement, taggedWithVowel)
		print(result)
		results.append(result)

	print('Mean:')
	print(reduce(lambda x, y: x + y, results) / len(results))
	print('Stdev:')
	print(statistics.stdev(results))
