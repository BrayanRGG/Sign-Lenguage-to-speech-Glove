import numpy as np
import serial

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

ser = serial.Serial(port='COM4', baudrate='9600', bytesize=serial.EIGHTBITS, parity=serial.PARITY_NONE, timeout=2)
try:
	ser.isOpen()
	print("Serial port is open")
except:
	print("Error")
	exit()

NN = Neural_Network()

if(ser.isOpen()):
	try:
		while(1):
			ser.write(b'1')
			code = ser.readline()
			decode = code.decode('utf-8')
			print(decode);
			rdecoded = [float(x) for x in decode.split(',')]
			############################################################
			xPredicted = np.array((rdecoded), dtype=float)
			rl = NN.Obtain()
			print(rl)

	except EXCEPTION:
		print("Error")

else:
	print("Cannot Open Serial Port")
