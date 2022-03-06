l=int(input("enter limit:"))
a,b=0,1
for i in range(1,l+1):
    print(a,end='\t')
    
    a,b=b,a+b
