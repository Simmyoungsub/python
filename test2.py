# -*- coding: utf-8 -*-

import numpy as np
import numpy.linalg as lin

x = np.array([[1,2,3],[4,5,6]])
y = np.array([[1,0,-1],[1,1,0]])

print x
print y

#T is 전치행렬
np.dot(x,y.T) 

#역행렬
exlnv = np.array([[2,2,0],[-2,1,1],[3,0,1]])
result = lin.inv(exlnv)
print result
