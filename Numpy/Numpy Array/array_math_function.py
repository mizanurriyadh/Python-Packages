import numpy as np

x = np.array([[1,2],[3,4]])
y = np.array([[5,6],[7,8]])

print(x+y)
print(np.add(x,y))

print(x-y)
print(np.subtract(x,y))

print(np.multiply(x,y))

print(np.divide(y,x))

print(np.sqrt(y))