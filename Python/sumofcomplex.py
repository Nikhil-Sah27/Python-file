class complex:
    def __init__(self,real,image):
        self.real=real
        self.image=image
    def display(self):
        comp=f'{self.real}+{self.image}*i'
        print(comp)

    def sum(self):
        
        self.real=c1.real+c2.real
        self.image=c1.image+c2.image
    def disp(self):
        print(f'{self.real}+{self.image}*i')   
real=int(input("Input integer"))
image=int(input("Input integer"))
c1=complex(real,image)
real=int(input("Input integer"))
image=int(input("Input integer"))
c2=complex(real,image)
c1.display()
c1.sum()
c2.display()
c1.disp()