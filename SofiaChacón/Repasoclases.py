 #########Repaso clases 
import numpy as np
 
class ManejoMatriz():
    """
    Clase para calcular el determinante de una matriz de dim n 

    """
    def __init__(self,dim):
        self.dim=dim
        self.matriz=np.random.randint(0,10,(self.dim,self.dim)) 
        self.rango = range(self.dim)
    
    def cal_DET(self):
        determimante=  self.matriz[3][2]
        return self.matriz, determimante
        
    def cal_TS(self):
        y=self.rango
        Ts=list(map(lambda y: self.matriz[y][y:self.dim], y))
        return Ts
    
    

x =ManejoMatriz(4)
print(x.cal_DET())

y =ManejoMatriz.cal_DET(4)
print(y)