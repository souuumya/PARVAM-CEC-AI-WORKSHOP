# Numpy is used for Fast Mathematical Operations & to work with arrays.

# Importing the numpy library
import numpy as np


# Creating Arrays using Numpy
arr1 = np.array([1, 2, 3])
print("1D Array:", arr1)


# Creating 2D arrays (matrices)
arr2 = np.array([[1, 2], [3, 4]])
print("2x2 Matrix:\n", arr2)

arr3 = np.array([[1, 3, 5], [2, 4, 6], [7, 8, 9]])
print("3x3 Matrix:\n", arr3)


# Mathematical Operations
a = np.array([2, 5, 8])
b = np.array([3, 7, 11])

print("Sum:", a + b)
print("Difference:", a - b)
print("Product:", a * b)
print("Division:", a / b)


# np.arange()
evenArr = np.arange(0, 20, 2)
print("Even numbers:", evenArr)

mulOf3 = np.arange(0, 30, 3)
print("Multiples of 3:", mulOf3)


# np.linspace()
arr4 = np.linspace(0, 1, 5)
print("Linspace 0 to 1:", arr4)

arr5 = np.linspace(0, 5, 10)
print("Linspace 0 to 5:", arr5)


# np.zeros()
zeros1 = np.zeros((2, 3))
print("Zeros (2x3):\n", zeros1)

zeros2 = np.zeros((3, 5))
print("Zeros (3x5):\n", zeros2)


# np.ones()
ones1 = np.ones((3, 2))
print("Ones (3x2):\n", ones1)

ones2 = np.ones((5, 4))
print("Ones (5x4):\n", ones2)


# shape
arr6 = np.array([[1, 2], [3, 4]])
print("Shape:", arr6.shape)

arr7 = np.array([[2, 5, 5], [6, 10, 4]])
print("Shape:", arr7.shape)

arr8 = np.array([[2, 5, 5, 8, 3], [6, 10, 4, 2, 3]])
print("Shape:", arr8.shape)


# ndim
print("Dimensions (2D):", arr8.ndim)

arr9 = np.array([6, 10, 4, 2, 3])
print("Dimensions (1D):", arr9.ndim)


# size
print("Size (1D):", arr9.size)
print("Size (2D):", arr8.size)


# reshape
arr10 = np.arange(6)
print("Reshape 2x3:\n", arr10.reshape(2, 3))
print("Reshape 3x2:\n", arr10.reshape(3, 2))

arr11 = np.arange(16)
print("Reshape 4x4:\n", arr11.reshape(4, 4))
print("Reshape 2x8:\n", arr11.reshape(2, 8))
print("Reshape 8x2:\n", arr11.reshape(8, 2))


# flatten
arr12 = np.array([[0, 1, 2, 3],
                  [4, 5, 6, 7],
                  [8, 9, 10, 11],
                  [12, 13, 14, 15]])
print("Flatten:", arr12.flatten())

arr13 = np.array([[2, 4, 6], [3, 6, 9]])
print("Flatten:", arr13.flatten())


# Mathematical functions
arr14 = np.array([2, 5, 7, 11, 16, 20])
print("Sum:", arr14.sum())
print("Mean:", arr14.mean())
print("Max & Min:", arr14.max(), arr14.min())
print("Standard Deviation:", arr14.std())


# Indexing
arr15 = np.array([2, 7, 14, 5, 6])
print("Element at index 3:", arr15[3])


# 2D Indexing
arr16 = np.array([[2, 4, 6], [3, 6, 9]])
print("Element [1,2]:", arr16[1, 2])
print("Element [0,1]:", arr16[0, 1])


# Boolean Indexing
arr17 = np.array([1, 3, 2, 5, 6, 8])
print("Greater than 3:", arr17[arr17 > 3])
print("Less than 3:", arr17[arr17 < 3])
print("Even numbers:", arr17[arr17 % 2 == 0])


# random.rand()
randArr = np.random.rand(3, 3)
print("Random floats:\n", randArr)


# random.randint()
randIntArr = np.random.randint(0, 9, 6)
print("Random integers:", randIntArr)


# concatenate()
a1 = np.array([2, 3, 6])
b1 = np.array([3, 6, 10, 15, 19])
print("Concatenated:", np.concatenate((a1, b1)))


# unique()
arr18 = np.array([2, 4, 2, 3, 5, 4, 3, 6])
print("Unique values:", np.unique(arr18))


# sort()
arr19 = np.array([5, 3, 1, 2, 6, 3, 7, 4])
print("Sorted array:", np.sort(arr19))