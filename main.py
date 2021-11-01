import numpy as np

N = float(input("Masukkan jumlah baris: "))
M = float(input("Masukkan jumlah kolom matriks: "))

A = np.empty([int(N),int(M)])

for i in range(int(N)):
  for j in range(int(M)):
      A[i][j] = float(input("Masukkan elemen matriks baris ke-" + str(i+1) + " dan kolom ke-" + str(j+1) +" : "))