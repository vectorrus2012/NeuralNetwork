import FileReader
from NeuralNetwork import NeuralNetwork
import numpy

input_nodes = 784
hidden_nodes = 100
output_nodes = 10

learning_rate = 0.3

n = NeuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# train the neural network

print("start training...")

# small train set
train_data_list = FileReader.read_file("data/mnist_train_100.csv")

# uncomment and download full train data
# train_data_list = FileReader.read_file("data/mnist_train.csv")

for record in train_data_list:
    all_values = record.split(',')  # split the record by the ',' commas

    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01  # scale and shift he inputs

    targets = numpy.zeros(output_nodes) + 0.01

    targets[int(all_values[0])] = 0.99

    n.train(inputs, targets)
    pass

# test the neural network

print("start testing...")

# small data set
test_data_list = FileReader.read_file("data/mnist_test_10.csv")

# uncomment and download full test data
# test_data_list = FileReader.read_file("data/mnist_test.csv")

scorecard = []

# go through all the records in the test data set
for record in test_data_list:

    all_values = record.split(',')  # split the record by the ',' commas

    correct_label = int(all_values[0])  # correct answer is the first label
    # print(correct_label, " is correct value")

    # scale and shift the inputs
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01

    # query the network
    outputs = n.query(inputs)

    # the index of the highest value corresponds to the label
    label = numpy.argmax(outputs)
    # print(label, " is networks answer")

    # append correct or incorrect answer to list
    if label == correct_label:
        scorecard.append(1)
    else:
        scorecard.append(0)
        pass

    pass

# print(scorecard)

# calculates the performance score, the fraction of correct answers
scorecard_array = numpy.asarray(scorecard)
performance = scorecard_array.sum() / scorecard_array.size
print("performance = ", performance)