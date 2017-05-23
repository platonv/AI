from random import randint
from random import random
from functools import *
import statistics
import math

class Particle:
    def __init__(self):
        self.pos = [randint(-10, 10) for _ in range(2)]
        self.velocity = 0
        self.fitness = self.evaluate()
        self.bestPosition = self.pos
        self.bestFitness = self.fitness


    def evaluate(self):
        x = self.pos[0]
        y = self.pos[1]
        a = -20*math.pow(math.exp(1), -0.2*math.sqrt(0.5*(x*x+y*y))) - math.pow(math.exp(1), 0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.exp(1) + 20
        return a

    def update(self,particle):
        s = 1 / (1 + math.pow((math.exp(1)), -particle.velocity))
        for i in range(2):
            if (random() > s):
                self.pos[i] = randint(-10, 10)
            self.fitness = self.bestFitness

class Swarm:
    def __init__(self):
        self.v=[Particle() for i in range(40)]
        self.numberOfParticles = 40
        # print(self.v[1].pos)

    def getBestNeighbour(self,particle):
        return particle

    def getBestParticles(self):
        s = sorted(self.v, key = lambda x:x.evaluate(), reverse=True)
        self.v = s
        return s[-1]


class Controller:

    def __init__(self, population):
        self.population = population
        self.fileName = 'parameters.txt'

    def iteration(self):
        best = 0
        inertia = 0.5
        clf = 0.4
        slf = 0.5
        new_velocity = 0
        for i in range(len(self.population.v)):
            if self.population.v[i].bestFitness > self.population.v[best].bestFitness:
                best = i
        for i in range(len(self.population.v)):
            new_velocity = inertia * self.population.v[i].velocity
            new_velocity += clf * random() * (sum(self.population.v[i].bestPosition) - sum(self.population.v[i].pos))
            new_velocity += slf * random() * (sum(self.population.v[best].bestPosition) - sum(self.population.v[i].pos))
            trial = sum(self.population.v[i].pos) + new_velocity
            aux = self.population.v[best]
            if trial > 0 and trial < 7:
                new_velocity = self.population.v[i].velocity
                aux = self.population.v[i]
            # self.population.v[i].velocity = new_velocity
            print(self.population.v[i].pos, " before")
            # self.population.v[i].update(aux)
            print(self.population.v[i].pos, " after")
        return self.population.getBestParticles()


    def runAlg(self, nu):
        pop = self.iteration()
        for _ in range(nu):
            pop = self.iteration()
        return pop

    def loadParameters(self):
        with open(self.fileName, 'r') as f:
            self.n = int(f.readline().strip())
        f.close()


if __name__ == "__main__":
    s = Swarm()
    c = Controller(s)
    c.runAlg(50)

    results = []
    s = Swarm()
    c = Controller(s)
    for i in range(0,30):
        current = c.runAlg(i)
        print("Best", current.pos, " value " + str(current.bestFitness))
        results.append(current.bestFitness)
        print('Mean:')
    print(reduce(lambda x, y: x + y, results) / len(results))
    print('Stdev:')
    print(statistics.stdev(results))
