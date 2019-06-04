import numpy as np

xa = np.zeros((2,9),dtype=int)
y = np.array(([1, 2, 3, 4, 5, 6, 7, 8, 100],[ 10,1,32,4,5,5463,3,654,6]),dtype=int)

xPredicted = np.array(([0.836142,    1,   1,   0.889866,    0.90989]), dtype=float)
xy = np.zeros((200,5),dtype=float)
i=0

while(i<200):
	j=0
	while(j<5):
		xy[i,j] = xPredicted[j]
		j=j+1
	i=i + 1

print (xy)