import numpy as np

xPredicted = np.array(([0.730159, 0.765324,	0.929426, 0.880586,	0.863492]), dtype=float)

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
		return self.rl

	def forward(self, X):
		self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 3x2 weights
		self.z2 = self.sigmoid(self.z) # activation function
		self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
		o = self.sigmoid(self.z3) # final activation function
		return o

	def Predict(self):
		print("Predicted data based on trained weights:");
		print("Input (scaled): \n" + str(xPredicted));
		self.letter = ((self.forward(xPredicted))*5)
		print("Output: \n" + str(self.letter));
		self.rl = round(self.letter)
		print("Rounded Output: \n" + str(self.rl));


NN = Neural_Network()
rl = NN.Obtain()

thisdict =	{
  1: "A",
  2: "E",
  3: "I",
  4: "O",
  5: "U"
}

print(thisdict[rl]);