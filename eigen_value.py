import numpy as np
from sympy import symbols, Symbol, Poly, Matrix

def left_singular(A):
    At = A.transpose()
    return A.dot(At)

def right_singular(A):
    At = A.transpose()
    return At.dot(A)

def eigen_value_left(A):
    x = Symbol('x')
    left = left_singular(A)
    I = np.array([[x for i in range(len(left))]for j in range(len(left))])
    for k in range(len(A)):
        for l in range(len(A)): 
            if(k != l ):
                I[k][l] = 0
    temp = I - left
    temp = Matrix(temp)
    det = temp.det()
    det = Poly(det, x)
    value = np.roots(det.all_coeffs())
    value[::-1].sort()
    return value

def eigen_value_right(A):
    x = Symbol('x')
    right = right_singular(A)
    I = np.array([[x for i in range(len(right))]for j in range(len(right))])
    for k in range(len(right)):
        for l in range(len(right)): 
            if(k != l ):
                I[k][l] = 0
    temp = I - right
    temp = Matrix(temp)
    det = temp.det()
    det = Poly(det, x)
    value = np.roots(det.all_coeffs())
    value[::-1].sort()
    return value