s=int(input("Enter start range:"))
e=int(input("Enter end range:"))
c=0
for i in range(s,e+1):
    st=str(i)
    if len(st)==4:
        for d in st:
            if int(d)%2!=0:
                c=1
                break
            else:
                 c=2
        if c==2 and (int(i**0.5))**2==i:
            print(i)

            
            
            
