# Data normalization
  # 1. Statistical:
    # S - sample data
    # m - average of S
    # std - standard deviation of S
    # => v = (v - m) / std, v of S

  # 2. min - max:
    # m - min(S)
    # M - max(S)
    # => v in  [m, M] => v1 in [vMin, vMax]

    # v1 = vMin + (v - m) / (M - m) * (vMax - vMin)

class Neuron:
    def __init__(self, n):
        self.nInputs = n
        self.w = [random() * 2 - 1 for i in range(self.nInputs)]
        self.o = 0
        self.err = 0

    def activate(self, n):
        s = sum([u[i] * self.w[i] for i in range(self.nInputs)])
        # For linear
        self.o = s
        # For sigmoid
        self.o = 1 / (1 + exp(-s))

    def setError(self, v):
        # For linear
        self.err = v
        # For sigmoid
        self.err = self.o * (1 - self.o) * v

class Layer:
    def __init__(self, m, n):
        self.nNeuron = m
        self.neurons = [Neuron(n) for k in range(1, self.nNeuron)]

class Network:
    def __init__(self, a, b, c, d):
        self.nInputs = a
        self.nOutputs = b
        self.nNPHL = c # number of neurons per hidden layer
        self.nHL = d # number of hiddend layers

        # Input layer
        self.layers = [Layer(self.nInputs, 0)]
        # First hidden Layer
        self.layers += [Layer(self.nNPHL, self.nInputs)]
        # Other thidden layers
        self.layers += [Layer(self.nNPHL, self.nNPHL) for k in range(self.nHL - 1)]
        # Output layer
        self.layers += [Layer(self.nOutputs, self.nNPHL)]

    def activate(self, u):
        i = 0
        for n in self.layers[0].neurons:
            n.o = u[i]
            i += 1

        for l in range(1, self.nHL + 2):
            info = [n2.o for n2 in self.layers[l - 1].neurons]
            for n in self.layers[l].neurons:
                n.activate(info)

    def errorBackPropagate(self, error):
        for l in range(self.nHL + 1, 0, -1):
            i = 0
            for n in self.layers[l].neurons:
                if l == self.nHL + 1:
                    n.setError(error[i])
                else:
                    s = sum([n2.w[i] * n2.err for n2 in self.layers[l + 1].neurons])
                    n.setError(s)
                i += 1

                for j in range(n.nInputs)
                    n.w[j] = n.w[j] * learning_rate * n.err * self.layers[l - 1].neurons[j].o
