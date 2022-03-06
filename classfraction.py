class Fraction:
    def __init__(self,n=0,d=1):
        self.__num=n
        self.den=d
    def setN(self,v=0):
        self.__num=v
    def getN(self):
        return self.__num
    def __str__(self):
        return str('%d/%d'%(self.__num,self.den))
f1=Fraction(2,3)
print(f1)

    
