#simple linear regression using gradient descent
import numpy as np
import matplotlib.pyplot as plt
# generate random data-set
observations = 1000
xs = np.random.uniform(low=-10, high=10, size=(observations, 1))
zs = np.random.uniform(-10, 10, (observations, 1))
inputs = np.column_stack((xs, zs))
print(inputs.shape)
# create targets we will aim at
noise = np.random.uniform(-1, 1, (observations, 1))
targets = 2*xs - 3*zs + 5 + noise
print(targets.shape)
# initialize variables
init_range = 0.1
weights = np.random.uniform(-init_range, init_range, size=(2, 1))
biases = np.random.uniform(-init_range, init_range, size=1)
print(weights)
print(biases)
# set a learning rate
learning_rate = 0.02
# train the model
for i in range(100):
    outputs = np.dot(inputs, weights) + biases
    deltas = outputs - targets
    loss = np.sum(deltas ** 2) / 2 / observations
    print(loss)
    deltas_scaled = deltas / observations
    weights = weights - learning_rate * np.dot(inputs.T, deltas_scaled)
    biases = biases - learning_rate * np.sum(deltas_scaled)
# print(weights, biases)
# plot the last output vs targets
plt.plot(outputs, targets)
plt.xlabel('outputs')
plt.ylabel('targets')
plt.show()
# plot the loss
plt.plot(loss)
plt.xlabel('loss')
plt.ylabel('loss')
plt.show()
