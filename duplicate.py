l=input("Enter numbers:").split()
dup=set()
uni=[]
for x in l:
    if x not in dup:
        uni.append(x)
        dup.add(x)
print(uni)

