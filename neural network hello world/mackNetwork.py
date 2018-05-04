
import numpy as np

# Neural network class based off Michael Nielsen's neural network book:
# http://neuralnetworksanddeeplearning.com/
# This class defines the structure of a neural network only,
# without any functions for training or data input yet.
class Network(object):
    def __init__(self,sizes):
        self.sizes = sizes
        self.layers = len(sizes)

        # for each layer except the first layer, create an array of dimension (rows=nodes, cols=1) with
        # random numbers with a mean of 0 and stddev the default for np.random.randn
        self.biases = []
        for layer in range(1,self.layers):
            self.biases.append( np.random.randn(sizes[layer],1) )

        # for each layer except the first layer, create an array of dimension (rows=#nodes, cols=#prev layer nodes)
        # with random numbers with a mean of 0.
        self.weights = []
        for i in range(1,self.layers):
            self.weights.append( np.random.randn(sizes[i],sizes[i-1]) )


from matplotlib import pyplot
# Defines printer object to display neural network.
# Input argument is a single neural network object
class Printer(object):
    def __init__(self, net):
        self.net = net

        self.x = 10
        self.y = 10
        self.neuron_radius = 0.5

        self.horizontal_space = 10
        self.vertical_space = 3

        self.n_lines = 0 # Count the number of lines in the neural network
        for i in range(1,self.net.layers):
            self.n_lines += self.net.sizes[i-1] * self.net.sizes[i]

        self.color_idx = np.linspace(0, 1, self.n_lines)

    # Displays the neural network using matplotlib
    def netPrint(self):
        color_index = 0
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
                        pyplot.gca().plot([x, x-self.horizontal_space-0.5], [y, -n*self.vertical_space],
                                          color=self.colorGen(color_index),linestyle=self.lineGen(color_index),
                                          linewidth=1,label=str(round(self.net.weights[layer-1][node][n],3)))
                        color_index += 1
                    pyplot.gca().annotate(str(round(self.net.biases[layer-1][node],3)), xy=(x, y+.5), size=8)

                node_place += self.vertical_space
            layer_x_coord += self.horizontal_space

    # Returns a color to draw a line with
    # Examples of other color options to use besides hsv are Paired, jet, rainbow,
    # Example usage: return pyplot.cm.rainbow(self.color_idx[i])
    def colorGen(self,i):
        # return "b"
        return pyplot.cm.hsv(self.color_idx[i])

    # Returns a line type to draw a line with (ie. dot, dash)
    def lineGen(self,i):
        lines = ['-','--','-.',':']
        return lines[i%4]


    # Attach legend and show neural network
    def show(self):
        pyplot.gca().legend(loc='center left', bbox_to_anchor=(1, 0.3))
        pyplot.show()

a = Network([2,6,1]) # Initialize network with 3 layers with 2 nodes, 6 nodes, and 1 node.

p = Printer(a)
p.netPrint()
p.show()