#!/bin/python3
from collections import deque
from math import sin, cos, sqrt, exp, pi
from random import randint
from random import random, uniform
from functools import *
import statistics
import math

omega = 0.4
phiP = 0.025
phiG = 0.025
population = 100
iterations = 1000
particleSize = 3
xMin = -10
xMax = 10
yMin = -10
yMax = 10

def ackley(x, y):
    return -20*math.pow(math.exp(1), -0.2*math.sqrt(0.5*(x*x+y*y))) - math.pow(math.exp(1), 0.5*(math.cos(2*math.pi*x) + math.cos(2*math.pi*y))) + math.exp(1) + 20

class Vec2:
    def __init__(self, _x = 0, _y = 0):
        self.x = _x
        self.y = _y

    def __repr__(self):
        return self.x + ' ' + self.y

class Particle:
    def __init__(self, swarm):
        self.pos = Vec2(uniform(xMin, xMax), uniform(yMin, yMax))
        self.velocity = Vec2()
        self.bestPosition = self.pos
        self.fitness = ackley(self.pos.x, self.pos.y)
        self.bestFitness = self.fitness
        self.swarm = swarm

    def updateVelocity(self, p, g):
        newX = omega + self.velocity.x + phiP * p * self.bestPosition.x - self.pos.x + phiG * g * self.swarm.bestPosition.x - self.pos.x
        newY = omega + self.velocity.y + phiP * p * self.bestPosition.y - self.pos.y + phiG * g * self.swarm.bestPosition.y - self.pos.y
        self.velocity.x = newX
        self.velocity.y = newY

    def updatePosition(self):
        newX = max(min(self.pos.x + self.velocity.x, xMax), xMin)
        newY = max(min(self.pos.y + self.velocity.y, yMax), yMin)
        self.pos.x = newX
        self.pos.y = newY
        self.fitness = ackley(self.pos.x, self.pos.y)

        if self.fitness < self.bestFitness:
            self.bestFitness = ackley(self.pos.x, self.pos.y)
            self.bestPosition = self.pos

    def notifyBestPosition(self):
        self.bestPosition = self.pos

class Swarm:
    def __init__(self):
        self.particles = [Particle(swarm=self) for _ in range(population)]
        self.bestPosition = Vec2()
        self.bestFitness = min([x.fitness for x in self.particles])

    def iterate(self):
        for particle in self.particles:
            p, g = random(), random()
            particle.updateVelocity(p, g)
            particle.updatePosition()

            if particle.bestFitness < self.bestFitness:
                self.bestPosition = particle.bestPosition
                self.bestFitness = particle.bestFitness
        print(self.bestFitness)

class Controller:

    def __init__(self, swarm):
        self.swarm = swarm

    def runAlg(self):
        for _ in range(iterations):
            self.swarm.iterate()

if __name__ == "__main__":
    s = Swarm()
    c = Controller(s)
    c.runAlg()

    # results = []
    # s = Swarm()
    # c = Controller(s)
    # for i in range(0,30):
    #     current = c.runAlg(i)
    #     print("Best", current.pos, " value " + str(current.bestFitness))
    #     results.append(current.bestFitness)
    # print('Mean:')
    # print(sum(results) / len(results))
    # print('Stdev:')
    # print(statistics.stdev(results))
