import math
import skimage.io
import numpy as np
import matplotlib.pyplot as plt

a_point1 = np.array([0, 1, 1])
a_point2 = np.array([0, 3, 1])

a_martix = np.array([[1, 0, 2],
                     [0, -1, -1],
                     [0, 0, 1]])

print("a", np.matmul(a_martix, a_point2))

b_point1 = np.array([1, 1, 1])
b_point2 = np.array([0, 0, 1])
b_point3 = np.array([0, 1, 1])
b_point4 = np.array([1, 0, 1])

b_martix = np.array([[2, 4, 1],
                     [2, 2, 1],
                     [0, 0, 1]])

print("b_point1", np.matmul(b_martix, b_point1))
print("b_point2", np.matmul(b_martix, b_point2))
print("b_point3", np.matmul(b_martix, b_point3))
print("b_point4", np.matmul(b_martix, b_point4))

c_point1 = np.array([2, 2, 1])
c_point2 = np.array([3, 1, 1])

c_martix = np.array([[0.981, -0.195, 0],
                     [-0.195, 0.981, 0],
                     [0.0, 0, 1]])

print("c_point1", np.matmul(c_martix, c_point1))
print("c_point2", np.matmul(c_martix, c_point2))
