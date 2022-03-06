l=list(map(int,input("Enter numbers:").split()))
for i in l:
    if i>100:
        l[l.index(i)]='OVER'
print(*l,sep=", ")
