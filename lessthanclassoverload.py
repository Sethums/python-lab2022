class Rectangle:
    def __init__(self,l=0,w=0):
        self.__len=l
        self.__wid=w
    def __lt__(self,other):
        if (self.__len*self.__wid) < (other.__len*other.__wid):
            return True
        else:
            return False
try:
    r1=Rectangle(4,3)
    r2=Rectangle(2,3)
    if r1<r2:
        print("Area of Rectangle 1 less")
    else:
        print("Area of rect 2 is less")
except Exception as e:
    print(e)
    
