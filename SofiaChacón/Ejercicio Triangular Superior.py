import numpy as np
##Funcion para retornar los elementos de la triangular superior
def Ts(dim):
    matriz = np.random.randint(0,10,(dim,dim))
    y = range(dim)
    Ts=list(map(lambda y: matriz[y][y:dim], y))
    return (matriz, Ts)
dim=10
matriz, Ts= Ts(dim)
print(matriz, Ts)
