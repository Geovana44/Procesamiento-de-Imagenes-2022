import numpy as np
class kernels():
 
    def __init__(self,x,y,X,Y,OUT):
        self.x = x
        self.y = y
        self.X = X
        self.Y = Y
        self.OUT = OUT
    def Linear_Kernel(self):
      #x = np.asarray([1, 4.5, 0.8, 5.7, 4.2])#x.shape = (5,1)# dimension: 5x1
      #y = np.asarray([0.5, 2.5, 3.8, -5.7, -2.2])# dimension: 1x5
      T=5# se toma como constante(es una pregunta)
      c=2#se toma como constante
      N = 10
      P = 5

      a=(self.x**T)*self.y+c  # dimension: 5x5
      #return a

      X = np.random.randn(N,P)
      Y = np.random.randn(N,P)

      OUT = np.zeros((N,N))

      for i in range(N):
        mult = (X[i,...]**T)*Y # R{NXP}
        q=mult
        q=q
        a = q+c 
        return a 
    def KERNEL2(self):
      c=4

      x_x_ = self.x - self.y # 1dim p elemntos
      norm = np.linalg.norm(x_x_, ord=2) #scalar
      norm = norm**2 #sca
      div = (norm+c**2)**(1/2) #scarlar

      #N = 10
      #P = 5

      #X = np.random.randn(N,P)
      #Y = np.random.randn(N,P)

      #OUT = np.zeros((N,N))

      for i in range(N):
        resta = self.X[i,...] - self.Y # R{NXP}
        norm = np.linalg.norm(resta, ord=2, axis=1) #R{N}
        norm = norm**2 #R{N}
        div = (norm+c**2)**(1/2) #R{N}
        OUT[i, ...] = div
        return  OUT[i, ...] 
    
    def  KERNEL3(self):
      d=3
        
    def KERNEL4(self):
      x=1
        
    def KERNEL5(self):
        2
    def KERNEL6(self):
      4
    def  KERNEL7(self):
        3
     
    def KERNEL8(self):
      2

    def KERNEL9(self):
      4

    def KERNEL10(self):
      3


#a = float(input('Ingrese el primer numero : '))
#b = float(input('Ingrese el segundo numero: '))        
x = np.asarray([1, 4.5, 0.8, 5.7, 4.2])
y = np.asarray([0.5, 2.5, 3.8, -5.7, -2.2])
N = 10
P = 5
X = np.random.randn(N,P)
Y = np.random.randn(N,P)
OUT = np.zeros((N,N))
obj=kernels(x,y,X,Y,OUT)
while True:
    def menu():
        w = ('1.Linear_Kernel\n2. KERNEL2 \n3.  KERNEL3 \n4.  KERNEL4\n5. KERNEL5  \n6. KERNEL6\n7. KERNEL7\n8. KERNEL8\n9. KERNEL9\n10. KERNEL10') 
        print(w)
    menu()
    Op = int(input('Seleccione una opcion de la siguiente lista : ')) 
    if Op == 1:
        print("Resultado: ",obj.Linear_Kernel())
    elif Op == 2:
        print("Resultado: ",obj.KERNEL2())
    elif Op == 3:
        print("Resultado: ",obj.KERNEL3())    
    elif Op == 4:
      print("Resultado: ",obj.KERNEL4())
    elif Op == 5:
      print("Resultado: ",obj.KERNEL5())
    elif Op == 6:
        print("Resultado: ",obj.KERNEL6())  
    elif Op == 7:
        print("Resultado: ",obj.KERNEL7())
    elif Op == 8:
        print("Resultado: ",obj.KERNEL8())
          
    elif Op == 9:
        print("Resultado: ",obj.KERNEL9())
          
    elif Op == 10:
        print("Resultado: ",obj.KERNEL10())
          
    elif Op == 0:
        print('Vuelva a intentar')
        break
    else:
        print('Opcion Invalida') 
        break       
print()