import mnist_loader as ml
import network

training_data, validation_data, test_data = ml.load_data_wrapper()
#net = network.Network([784, 30, 10])
#net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
print "---------------------------"
net = network.Network([784, 30, 10])
net.SGD_improved(training_data, 30, 10, 3.0, test_data=test_data, lmbda=0.8)
# print "---------------------------"
# net = network.Network([784, 100, 10])
# net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
# print "---------------------------"
# net = network.Network([784, 100, 10])
# net.SGD(training_data, 30, 10, 0.001, test_data=test_data)  ## bad hyper-parameter
# print "---------------------------"
# net = network.Network([784, 30, 10])
# net.SGD(training_data , 30, 10, 100.0, test_data=test_data) # too high learn rate #it's too bad
# print "---------------------------"
# net = network.Network([784, 10])
# net.SGD(training_data, 30, 10, 3.0, test_data=test_data) #exercise from the book #achieved Epoch 29: 9164 / 10000