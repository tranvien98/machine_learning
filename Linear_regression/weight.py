from __future__ import print_function
import numpy as np 
import matplotlib.pyplot as plt 

#height (cm) input data each row is a data point

X = np.array([[147, 150, 153, 158, 163, 165, 168, 170, 173, 175, 178, 180, 183]]).T

# weight (kg)
y = np.array([ 49, 50, 51, 54, 58, 59, 60, 62, 63, 64, 66, 67, 68])
# print(X)
# Building Xbar
one = np.ones((X.shape[0], 1))
# print(one)
Xbar = np.concatenate((one, X), axis = 1)
# print(Xbar.T)
A = np.dot(Xbar.T, Xbar)
b = np.dot(Xbar.T, y)
print(Xbar.shape)
w = np.dot(np.linalg.pinv(A),b)

w_0 = w[0]
w_1 = w[1]

print("The height 155 have weight is: ", w_0 + w_1*155)
print("The height 160 have weight is: ", w_0 + w_1*160)
# The height 155 have weight is:  52.94135889480448
# The height 160 have weight is:  55.73738370451747
# table 155 - 52
#       160 - 56