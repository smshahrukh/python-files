from numpy import exp, array, random, dot
training_set_input = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_output = array([[0, 1, 1, 0]]).T
random.seed(1)
synaptic_weights = 2*random.random((3,1)) - 1
for i in xrange(10000):
    output = 1/(1+exp(-(dot(training_set_input, synaptic_weights))))
    synaptic_weights += dot(training_set_input.T, (training_set_output - output) * output * (1 - output))
print 1/(1+exp(-(dot(array([1,0,0]), synaptic_weights))))