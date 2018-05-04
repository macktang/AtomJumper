
import numpy as np

class Network(object):

    def __init__(self,sizes):
        self.sizes = sizes
        self.layers = len(sizes)

        # for each layer except the first layer, create an array of dimension (rows=nodes, cols=1) with
        # random numbers with a mean of 0.
        self.biases = []
        for layer in range(1,self.layers):
            self.biases.append( np.random.randn(sizes[layer],1) )

        # for each layer except the first layer, create an array of dimension (rows=#nodes, cols=#prev nodes) with
        # random numbers with a mean of 0.
        self.weights = []
        for i in range(1,self.layers):
            self.weights.append( np.random.randn(sizes[i],sizes[i-1]) )


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
        layer_x_coord = 0
        for layer in range(0,self.net.layers):
            node_place = 0

            for node in range(0,self.net.sizes[layer]):
                x = layer + layer_x_coord
                y = -node_place
                circle = pyplot.Circle((x, y), radius=self.neuron_radius, fill=False)
                pyplot.gca().add_patch(circle)
                if not layer == 0:
                    for n in range(0,self.net.sizes[layer-1]):
                        pyplot.gca().plot([x, x-self.horizontal_space], [y, -n*self.vertical_space], color='b',
                             linestyle='-', linewidth=1)
                    pyplot.gca().annotate(str(self.net.biases[layer - 1][node]), xy=(x, y), size=8)

                node_place += self.vertical_space
            layer_x_coord += self.horizontal_space


    def show(self):
        pyplot.axis('scaled')
        pyplot.show()

a = Network([2,6,1])

print a.biases
print a.weights

p = Printer(a)
p.netPrint()
p.show()