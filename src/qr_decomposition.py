import numpy as np

def find_eig_qr(A):  # fungsi untuk melakukan dekomposisi matriks dengan metode QR
    IQ = np.eye(A.shape[0])
    X=A.copy()
    for i in range(6):  # iterasi minimum untuk eigenvalue dan eigenvector yang mendekati dengan aslinya
            Q,R = np.linalg.qr(X)
            IQ = IQ @ Q;
            X = R @ Q;
    return np.diag(X), IQ # return eigenvalue dan eigenvector