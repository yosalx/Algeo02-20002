import numpy as np
from sympy import symbols, Symbol, Poly, Matrix

N = float(input("Masukkan jumlah baris: "))
M = float(input("Masukkan jumlah kolom matriks: "))

A = np.empty([int(N),int(M)])

for i in range(int(N)):
  for j in range(int(M)):
      A[i][j] = float(input("Masukkan elemen matriks baris ke-" + str(i+1) + " dan kolom ke-" + str(j+1) +" : "))

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


"""

Ini pas make power iteration

{def eigenvalue(A, v):
    Av = A.dot(v)
    return v.dot(Av)

#def power_iteration(A):
    n, d = A.shape

    v = np.ones(d) / np.sqrt(d)
    ev = eigenvalue(A, v)

    while True:
        Av = A.dot(v)
        v_new = Av / np.linalg.norm(Av)

        ev_new = eigenvalue(A, v_new)
        if np.abs(ev - ev_new) < 0.01:
            break

        v = v_new
        ev = ev_new
    
    return ev_new, v_new

#value,vector = power_iteration(left_singular(A))
"""


