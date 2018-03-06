import numpy as np

a = np.array([1,2,3])   # Create rank 1 array
print(type(a))          # Print numpy array type = "<class 'numpy.ndarray'>"
print(a.shape)          # Printing array shape
print(a[0], a[1], a[2]) # Prints Values of the array
a[0] = 5                # changing an element of the array
print(a)                # Printing whole array

b = np.array([[1,2,3],[4,5,6]])
print(b.shape)          # Printing "(2,3)"
print(b[0,0], b[0,1], b[1,2])   # Printing "1 2 6"
