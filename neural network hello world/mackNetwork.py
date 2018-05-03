
import numpy as np

class Network(object):

    def __init__(self,sizes):
        self.sizes = sizes
        self.layers = len(sizes)

        # for each layer except the first layer, create a tuple that contains dimension (rows=nodes, cols=1) with
        # random numbers with a mean of 0.
        self.biases = []
        for layer in range(1,self.layers):
            self.biases.append( np.random.randn(sizes[layer],1) )

        self.weights = []
        for weight in range(1,self.layers):
            self.weights.append( np.random.randn(sizes[layer],sizes[layer-1]) )


from matplotlib import pyplot

class Printer(object):
    def __init__(self, net):
        self.net = net

        self.x = 10
        self.y = 10
        self.neuron_radius = 0.5

        self.horizontal_space = 10
        self.vertical_space = 3

    def netPrint(self):
        for layer in range(0,self.net.layers):
            for node in range(0,)
        circle = pyplot.Circle((self.x, self.y), radius=self.neuron_radius, fill=False)
        pyplot.gca().add_patch(circle)

    def show(self):
        pyplot.axis('scaled')
        pyplot.show()

a = Network([2,6,1])

print a.biases
print a.weights

p = Printer(a)
p.netPrint()
p.show()