#5. Hallar la matriz simétrica
import numpy as np
import random
"""
Ejemplo de matrices simetricas llenar
[1,0],[0,1]

Ejemplo matriz no simetricas llenar

"""
A=[[1,0],[0,1]]

def transpuesta(A):
    m = np.array(A)
    B = np.transpose(m)
    print(m)
    print(B)
    for i in m:
        for j in m:
            if m[i][j]==B[i][j]:
                print ("simetrica")
            else:
                print("No es simetrica")
transpuesta(A)