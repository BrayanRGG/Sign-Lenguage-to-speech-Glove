import numpy as np

xPredicted = np.array(([0.836142,    1,   1,   0.889866,    0.90989]), dtype=float)

class Neural_Network(object):

	def sigmoid(self, s):
    # activation function
		return 1/(1+np.exp(-s))

	def sigmoidPrime(self, s):
    #derivative of sigmoid
		return s * (1 - s)
	
	def Obtain(self):
		self.W1 = np.loadtxt("w1.txt")
		self.W2 = np.loadtxt("w2.txt")
		self.Predict()

	def Predict(self):
		print("Predicted data based on trained weights:");
		print("Input (scaled): \n" + str(xPredicted));
		print("Output: \n" + str((self.forward(xPredicted))*5));

	def forward(self, X):
		self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
		self.z2 = self.sigmoid(self.z) # activation function
		self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
		o = self.sigmoid(self.z3) # final activation function
		return o

NN = Neural_Network()
NN.Obtain()


		
		