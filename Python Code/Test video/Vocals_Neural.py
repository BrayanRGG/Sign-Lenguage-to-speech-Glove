import numpy as np

# X = Valores de referencia, y = Resultado, xPredicted = Datos de letra U para predecir
A = [1, 0.596446154, 0.594261538, 0.596446154, 0.567853846]
E = [0.6, 0.562749164, 0.610612709, 0.624120067, 0.614790301]
I = [0.8, 0.587176589, 0.627032441, 0.641683946, 1]
O = [1, 0.770496488, 0.752656187, 0.843158863, 0.727092308]
U = [0.716539164, 1, 0.997886622, 0.682747492, 0.664662207]

X = np.array((A, E, I, O, U), dtype=float)
y = np.array(([1], [2], [3], [4], [5]), dtype=float)

xPredicted = np.array(([0.836142,    1,   1,   0.889866,    0.90989]), dtype=float)#U

y = y/5 # Existen 5 letras y normalizaremos los valores en el rango de 0-1 para trabajar con ellos
########################INICIO DE DECLARACION DE CLASE##########################################
class Neural_Network(object):
  def __init__(self):
    #Parametros de la red neuronal
    self.inputSize = 5
    self.outputSize = 1
    self.hiddenSize = 3

    #Pesos
    self.W1 = np.random.randn(self.inputSize, self.hiddenSize) # (5x3) Matriz de pesos para la entrada
    self.W2 = np.random.randn(self.hiddenSize, self.outputSize) # (5x3) Matriz de pesos para la salida

  def forward(self, X):
    #Funcion de "Forward Propagation"
    self.z = np.dot(X, self.W1) # dot product of X (input) and first set of 5x3 weights
    self.z2 = self.sigmoid(self.z) # Funcion de activacion
    self.z3 = np.dot(self.z2, self.W2) # dot product of hidden layer (z2) and second set of 3x1 weights
    o = self.sigmoid(self.z3) # final Funcion de activacion
    return o

  def sigmoid(self, s):
    # Funcion de activacion
    return 1/(1+np.exp(-s))

  def sigmoidPrime(self, s):
    #Derivada de Sigmoid
    return s * (1 - s)

  def backward(self, X, y, o):
    # Backward Propagation en la red
    self.o_error = y - o # Error en la salida
    self.o_delta = self.o_error*self.sigmoidPrime(o) # Aplicando Derivada de Sigmoid al error

    self.z2_error = self.o_delta.dot(self.W2.T) #Que tanto los pesos de las salidas contribuyeron al error
    self.z2_delta = self.z2_error*self.sigmoidPrime(self.z2) # AplicandoDerivada de Sigmoid a z2 error

    self.W1 += X.T.dot(self.z2_delta) # Ajustando los primeros pesos (input --> hidden) 
    self.W2 += self.z2.T.dot(self.o_delta) #Ajustando los segundos pesos (hidden --> output) 

  def train(self, X, y):#Funcion de entrenamiento que llama a las demas
    o = self.forward(X)
    self.backward(X, y, o)

  def saveWeights(self):#Funcion para guardar los pesos en archivos w1.txt y w2.txt
    np.savetxt("w1.txt", self.W1, fmt="%s")
    np.savetxt("w2.txt", self.W2, fmt="%s")

  def predict(self):#Print de los valores recibidos 
    print ("Predicted data based on trained weights:");
    print ("Input (scaled): \n" + str(xPredicted));
    print ("Output: \n" + str((self.forward(xPredicted))*5));
########################FIN DE DECLARACION DE CLASE##########################################


NN = Neural_Network()#Declarando un objeto para la clase


for i in range(20000): # Entrena la red 20,000 veces
  print (" #" + str(i) + "\n")
  print ("Input (scaled): \n" + str(X))
  print ("Actual Output: \n" + str(y))
  print ("Predicted Output: \n" + str(NN.forward(X)))
  print ("Loss: \n" + str(np.mean(np.square(y - NN.forward(X))))) # mean sum squared loss
  print ("\n")
  NN.train(X, y)

NN.saveWeights()#Guarda los pesos finales
NN.predict()#Nos da la prediccion final para el ejemplo
