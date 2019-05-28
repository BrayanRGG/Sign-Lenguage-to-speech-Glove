import numpy as np

# X = (hours studying, hours sleeping), y = score on test, xPredicted = 4 hours studying & 8 hours sleeping (input data for prediction)
A = [0.855992722, 0.596446154, 0.594261538, 0.596446154, 0.567853846]
E = [0.63941204, 0.562749164, 0.610612709, 0.624120067, 0.614790301]
I = [0.660040559, 0.587176589, 0.627032441, 0.641683946, 0.978658528]
O = [0.865042809, 0.770496488, 0.752656187, 0.843158863, 0.727092308]
U = [0.716539164, 0.998996656, 0.997886622, 0.682747492, 0.664662207]

X = np.array((A, E, I, O, U), dtype=float)
y = np.array(([1], [2], [3], [4], [5]), dtype=float)

xPredicted = np.array(([0.836142,    1,   1,   0.889866,    0.90989]), dtype=float)

# scale units
#X = X/np.amax(X, axis=0) # maximum of X array
# xPredicted = xPredicted/np.amax(xPredicted, axis=0) # maximum of xPredicted (our input data for the prediction)
y = y/5 # max test score is 100

class Neural_Network(object):
  def __init__(self):
    #parameters
    self.inputSize = 5
    self.outputSize = 1
    self.hiddenSize = 3

    #weights
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (3x2) weight matrix from input to hidden layer
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (3x1) weight matrix from hidden to output layer

  def forward(self, X):
    #forward propagation through our network
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
    self.z2 = self.sigmoid(self.z) # activation function
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z3) # final activation function
    return o

  def sigmoid(self, s):
    # activation function
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    #derivative of sigmoid
    return s * (1 - s)

  def backward(self, X, y, o):
    # backward propgate through the network
    self.o_error = y - o # error in output
    self.o_delta = self.o_error*self.sigmoidPrime(o) # applying derivative of sigmoid to error

    self.z2_error = self.o_delta.dot(self.W2.T) # z2 error: how much our hidden layer weights contributed to output error
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # applying derivative of sigmoid to z2 error

    self.W1 += X.T.dot(self.z2_delta) # adjusting first set (input --> hidden) weights
    self.W2 += self.z2.T.dot(self.o_delta) # adjusting second set (hidden --> output) weights

  def train(self, X, y):
    o = self.forward(X)
    self.backward(X, y, o)

  def saveWeights(self):
    np.savetxt("w1.txt", self.W1, fmt="%s")
    np.savetxt("w2.txt", self.W2, fmt="%s")

  def predict(self):
    print ("Predicted data based on trained weights:");
    print ("Input (scaled): \n" + str(xPredicted));
    print ("Output: \n" + str((self.forward(xPredicted))*5));


NN = Neural_Network()
for i in range(10000): # trains the NN 100,000 times
  print (" #" + str(i) + "\n")
  print ("Input (scaled): \n" + str(X))
  print ("Actual Output: \n" + str(y))
  print ("Predicted Output: \n" + str(NN.forward(X)))
  print ("Loss: \n" + str(np.mean(np.square(y - NN.forward(X))))) # mean sum squared loss
  print ("\n")
  NN.train(X, y)

NN.saveWeights()
NN.predict()
