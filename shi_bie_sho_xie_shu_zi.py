# import numpy
# import scipy.special
#
# # neural network class definition
# class neuralNetwork:
#
#     # initialise the neural network
#     def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
#         # set number of nodes in each input, hidden ,output layer
#         self.inodes = inputnodes
#         self.hnodes = hiddennodes
#         self.onodes = outputnodes
#
#         # link weight matrices, wih and who
#         # weights inside the arrays ars w_i_j,where link is from node i to node j in the next layer
#         # w11 w21
#         # w12 w22 etc
#         self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
#         self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))
#
#         # learning rate
#         self.lr = learningrate
#
#         # activation function is the sigmoid function
#         self.activation_function = lambda x: scipy.special.expit(x)
#
#         pass
#
#     # train the neural network
#     def train(self, inputs_list, targets_list):
#         # convert inputs list to 2d array
#         inputs = numpy.array(inputs_list, ndmin=2).T
#         targets = numpy.array(targets_list, ndmin=2).T
#
#         # calculate signals into hidden layer
#         hidden_inputs = numpy.dot(self.wih, inputs)
#         # calculate the signals emerging from hidden layer
#         hidden_outputs = self.activation_function(hidden_inputs)
#
#         # calculate signals into final output layer
#         final_inputs = numpy.dot(self.who, hidden_outputs)
#         # calculate the signals emerging from final output layer
#         final_outputs = self.activation_function(final_inputs)
#
#         # output layer error is the (target - actual)
#         output_errors = targets - final_outputs
#         # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
#         hidden_errors = numpy.dot(self.who.T, output_errors)
#
#         # update the weights for the links between the hidden and output layers
#         self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
#                                         numpy.transpose(hidden_outputs))
#
#         # update the weights for the links between the input and hidden layers
#         self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
#                                         numpy.transpose(inputs))
#
#         pass
#
#         # query the neural network
#
#     def query(self, inputs_list):
#         # convert inputs list to 2d array
#         inputs = numpy.array(inputs_list, ndmin=2).T
#
#         # calculate signals into hidden layer
#         hidden_inputs = numpy.dot(self.wih, inputs)
#         # calculate the signals emerging from hidden layer
#         hidden_outputs = self.activation_function(hidden_inputs)
#
#         # calculate signals into final output layer
#         final_inputs = numpy.dot(self.who, hidden_outputs)
#         # calculate the signals emerging from final output layer
#         final_outputs = self.activation_function(final_inputs)
#
#         return final_outputs
#
#
# # number of input, hidden and output nodes
# input_nodes = 3
# hidden_nodes = 3
# output_nodes = 3
#
# # learning rate is 0.3
# learning_rate = 0.3
#
# # create instance of neural network
# n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)
#
# # test query (doesn't mean anything useful yet)
# print(n.query([1.0, 0.5, -1.5]))


# 前馈神经网络
import numpy
import numpy as np

# neural network class definition
class NeuralNetwork:

    # initialise the neural network
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # set number of nodes in each input, hidden ,output layer
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes

        # link weight matrices, wih and who
        # weights inside the arrays ars w_i_j,where link is from node i to node j in the next layer
        # w11 w21
        # w12 w22 etc
        self.wih = numpy.random.normal(0.0, pow(self.inodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.onodes, self.hnodes))

        # learning rate
        self.lr = learningrate

        # activation function is the sigmoid function
        self.activation_function = lambda x: 1 / (1 + np.exp(-x))

        pass

    # train the neural network
    def train(self, inputs_list, targets_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        # output layer error is the (target - actual)
        output_errors = targets - final_outputs
        # hidden layer error is the output_errors, split by weights, recombined at hidden nodes
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # update the weights for the links between the hidden and output layers
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))

        # update the weights for the links between the input and hidden layers
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))

        pass

    # query the neural network
    def query(self, inputs_list):
        # convert inputs list to 2d array
        inputs = numpy.array(inputs_list, ndmin=2).T

        # calculate signals into hidden layer
        hidden_inputs = numpy.dot(self.wih, inputs)
        # calculate the signals emerging from hidden layer
        hidden_outputs = self.activation_function(hidden_inputs)

        # calculate signals into final output layer
        final_inputs = numpy.dot(self.who, hidden_outputs)
        # calculate the signals emerging from final output layer
        final_outputs = self.activation_function(final_inputs)

        return final_outputs

"""
初始化神经网络对象：创建一个 NeuralNetwork 的实例，指定输入层、隐藏层和输出层的节点数量以及学习率。
"""
# number of input, hidden and output nodes
input_nodes = 3
hidden_nodes = 3
output_nodes = 3

# learning rate is 0.3
learning_rate = 0.3

# create instance of neural network
n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

"""
训练神经网络：提供训练数据并使用 train 方法来训练神经网络。您需要将输入数据和目标数据提供给 train 方法，然后它会自动更新权重矩阵。
"""
# 提供训练数据并调用 train 方法
n.train(inputs_list, targets_list)


