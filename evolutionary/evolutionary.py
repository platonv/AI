#!/usr/bin/python3

import sys
from copy import deepcopy

class Individ:
	def __init__(self):
		pass

	def fitness(self, problem):
		pass

	def mutate(self, p):
		pass

	def crossover(individ1, individ2, p):
		pass

class Population:
	def __init__(self):
		pass

	def evaluate(self):
		pass

	def selection(self):
		pass

class Algorighm:
	def __init__(self):
		pass

class Problem:
	def __init__(self):
		pass

	def loadData(self, filename):
		pass

class Controller:
	def __init__(self, problem):
		self.problem = problem

class UI:
	def __init__(self, controller):
		self.controller = controller

	def mainMenu(self):
		pass

	def printHelp(self):
		print('usage: ./evolutionary.py <filename>')

class Application:
	def __init__(self):
		pass

if __name__ == '__main__':
	problem = Problem()
	problem.readFromFile(sys.argv[1])
	ui = UI(Controller(problem))
	ui.mainMenu()

