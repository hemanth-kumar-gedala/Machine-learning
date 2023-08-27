# -*- coding: utf-8 -*-
"""Untitled2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11VjdW2yG7q8OFas6KTpqkpdq7c_wWEwi
"""

import pandas as pd
import numpy as np
data=pd.read_excel(r"Lab Session1 Data.xlsx", sheet_name="Purchase data")
dataA=data.iloc[0:10,1:4]
matrixA=dataA.to_numpy()

dataC=data.iloc[0:10,4:5]
matrixC=dataC.to_numpy()

print("Matrix A = ")
print(matrixA)

print("Matrix C = ")
print(matrixC)

print("    ")
print("Rank of Matrix A  : ",np.linalg.matrix_rank(matrixA))

Ainverse=np.linalg.pinv(matrixA)

X=np.matmul(Ainverse,matrixC)


Cost=np.linalg.pinv(matrixA) @ matrixC
Au = np.hstack((matrixA, matrixC))
dimension=np.linalg.matrix_rank(Au)
print("Dimensionality :    ")
print(dimension)
print("   ")
print("Cost :  ")
print(Cost)