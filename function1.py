def analyse(num):
    return num>0,num==5
n=int(input("Enter number:"))
x=analyse(n)
if x[0]:
    print("Positive nm")
else:
    print("False")
if x[1]:
    print("Num is 5")
else:
    print("Notequals 5")
