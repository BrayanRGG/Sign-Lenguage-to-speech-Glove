import numpy as np

xa = np.zeros((2,9),dtype=int)
y = np.array(([1, 2, 3, 4, 5, 6, 7, 8, 100],[ 10,1,32,4,5,5463,3,654,6]),dtype=int)

maxInColumns = np.amin(y, axis=0)

print (maxInColumns)