import sys
class complex :
  def __init__(self,real,image):
    self.real=real
    self.image=image
  
  def addcomplex(x,y):
    real = x.real+y.real
    image=x.image+y.image
    return (complex(real,image))
    N= int(input("Enter the number of complex numbers to add:"))
    sum = complex(0,0)
    for i in range(N):
      real = int(input("Enter the real part of complex no.:"))
      image= int(input("Enter the imaginagry part of complex no.:"))
      sum =addcomplex(sum,complex(real,image))
      print("The sum of the complex number is ",sum.real,"+",sum.image,"i")
