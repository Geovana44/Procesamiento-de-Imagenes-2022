import numpy as np

class Recort():
  """
  Recortar imagen de forma rectangular

  Cut: recorta la imagen en escala de grises dentro de sus fonteras de forma

  """
  
  def __init__(self,Img):
    self.Img=Img
    self.C_Img=self.Img.copy()

  def Cut(self):
    self.H,self.V=np.where(self.Img < 255) #devuelve los indices de los pixeles q no son blanco
    self.C_Img=self.C_Img[min(self.H):max(self.H),min(self.V):max(self.V)] #Recorta la imagen

    return self.C_Img