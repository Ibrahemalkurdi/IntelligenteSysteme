import src.mnist_loader as ml
import src.network as network

training_data, validation_data, test_data = ml.load_data_wrapper()
net = network.Network([784, 30, 10])
net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
net.SGD_improved(training_data, 30, 10, 3.0, test_data=test_data, lmbda=0.3)

# ----------------
# net = network.Network([784, 100, 10])#one test was worse than 30 hidden neurons
# net.SGD(training_data, 30, 10, 3.0, test_data=test_data)
# ----------------
# net = network.Network([784, 100, 10])
# net.SGD(training_data, 30, 10, 0.001, test_data=test_data)  ## bad hyper-parameter
# ---------------
# net = network.Network([784, 30, 10])
# net.SGD(training_data , 30, 10, 100.0, test_data=test_data) # too high learn rate #it's too bad
# ----------------
# net = network.Network([784, 10])
# net.SGD(training_data, 30, 10, 3.0, test_data=test_data) #exercise from the book #achieved Epoch 29: 9164 / 10000
