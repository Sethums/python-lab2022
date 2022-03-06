class Rectangle:
    def __init__(self):
        self.__len=int(input("Enter length:"))
        self.wid=int(input("Enter width:"))
    def area(self):
        return self.__len*self.wid
    def peri(self):
        print('Perimeter of %d and %d is %d'%(getattr(self,'_Rectangle__len'),getattr(self,'wid'),2*(self.__len+self.wid)))
try:
    r1=Rectangle()
    print('Area of %d and %d is %d'%(getattr(r1,'_Rectangle__len'),getattr(r1,'wid'),r1.area()))
    r1.peri()
except Exception as e:
    print(e)
