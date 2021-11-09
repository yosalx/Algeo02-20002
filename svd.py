import numpy as np

# dummy SVD function

def svd(A):
    U = u_matrix(A)
    Sig = sig_matrix(A)
    Vt = v_matrix(A)
    return U,Sig,Vt



'''''
def eigen_vector_left(A):
    A = eigen_value_left(A)
    temp = np.empty([len(A),len(A)])
    for k in range(len(A)):
        left = left_singular(A)
        for i in range(len(left)):
            for j in range(len(left)):
                if i == j :
                    left[i][j] = A[k] - left[i][j]
'''     



#Ini pas make power iteration
#def eigenvalue(A, v):
    #Av = A.dot(v)
    #return v.dot(Av)
#def power_iteration(A):
    #n, d = A.shape
    #v = np.ones(d) / np.sqrt(d)
    #ev = eigenvalue(A, v)
    #while True:
        #Av = A.dot(v)
        #v_new = Av / np.linalg.norm(Av)
        #ev_new = eigenvalue(A, v_new)
        #if np.abs(ev - ev_new) < 0.01:
            #break
        #v = v_new
        #ev = ev_new
    #return ev_new, v_new
#value,vector = power_iteration(left_singular(A))