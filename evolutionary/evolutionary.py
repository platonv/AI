#!/usr/local/bin/python3

import sys
import random
from copy import deepcopy

class Individ:
    def __init__(self):
        self.v = [[i * 8 + k + 1 for k in range(8)] for i in range(8)]
        self.f = 0

    def fitness(self):
        f = 64
        for i in range(8):
            for j in range(8):
                if self._valid(i, j):
                    f -= 1
        self.f = f
        return f

    def _valid(self, i, j):
        val = self.v[i][j]
        try:
            if self.v[i + 2][j + 1] == val + 1:
                return True
        except:
            pass
        try:
            if self.v[i + 2][j - 1] == val + 1:
                return True
        except:
            pass
        try:
            if self.v[i - 2][j + 1] == val + 1:
                return True
        except:
            pass
        try:
            if self.v[i - 2][j - 1] == val + 1:
                return True
        except:
            pass
        try:
            if self.v[i + 1][j + 2] == val + 1:
                return True
        except:
            pass
        try:
            if self.v[i - 1][j + 2] == val + 1:
                return True
        except:
            pass
        try:
            if self.v[i + 1][j - 2] == val + 1:
                return True
        except:
            pass
        try:
            if self.v[i - 1][j - 2] == val + 1:
                return True
        except:
            pass
        return False

    def __str__(self):
        s = ''
        for x in range(8):
            s += str(self.v[x]) + '\n'
        return s

    def __repr__(self):
        return str(self)

class Population:
    def __init__(self, noInd):
        self.psize = noInd
        self.p = [Individ() for x in range(noInd)]

    def evaluate(self):
        for x in self.p:
            x.fitness()

    def selection(self, n):
        if n < self.psize:
            self.p = sorted(self.p, key = lambda Individual: Individual.f)
            self.p = self.p[:n]
            self.psize = n

    def reunion(self, toAdd):
        self.psize = self.psize + toAdd.psize
        self.p = self.p + toAdd.p

    def best(self, n):
        aux = sorted(self.p, key = lambda Individual: Individual.f)
        return aux[:n]

    def __str__(self):
        s = ''
        for x in self.p:
            s += x + '\n'
        return s

class Algorithm:
    def __init__(self, noI = 100, noG = 500):
        self.noInd = noI
        self.noGen = noG
        self.population = Population(noI)
        self.population.evaluate()

    def iteration(self):
        indexes = [i for i in range(self.noInd)]
        random.shuffle(indexes)
        no = self.noInd
        offspring = Population(no)
        for k in range(no):
            self.mutate(offspring.p[k])
        offspring.evaluate()
        self.population.reunion(offspring)
        self.population.selection(self.noInd)

    def run(self):
        for k in range(self.noGen):
            self.iteration()
        return self.population.best(1)[0]

    def crossover(self,i1,i2):
        pass

    def mutate(self, ind):
        for i in range(8):
            for j in range(8):
                if random.random() < 0.1:
                    ind.v[i][j], ind.v[random.randint(0,7)][random.randint(0,7)] = ind.v[random.randint(0,7)][random.randint(0,7)], ind.v[i][j]

class Controller:
    def __init__(self):
        self.alg = Algorithm()

    def runAlgorithm(self):
        return self.alg.run()

class UI:
    def __init__(self, controller):
        self.controller = controller

    def mainMenu(self):
        r = self.controller.runAlgorithm()
        print(r)
        print('Fitness: ' + str(r.f))

    def printHelp(self):
        print('usage: ./evolutionary.py <filename>')

class Application:
    def __init__(self):
        self.controller = Controller()
        self.ui = UI(self.controller)

    def run(self):
        self.ui.mainMenu()


if __name__ == '__main__':
    app = Application()
    app.run()

