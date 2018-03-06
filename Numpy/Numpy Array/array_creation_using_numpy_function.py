import numpy as np

a = np.zeros((2,2))         # Creating a nested array of all zeros
print(a)

b = np.ones((1,2))          # Creating an array of all ones
print(b)

c = np.full((2,2), 7)       # Creating a constant array
print(c)

d = np.eye(2)               # Creating (2*2) identity matrix
print(d)

e = np.random.random((5,3))  # Creating an array filled with random values
print(e)

