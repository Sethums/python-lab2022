s=input("Enter a sentence:").split()
l=0
c=0
for i in s:
    if len(i)>l:
        l=len(i)
        c=0
    elif len(i)==l:
        c=1
    else:
        c=2
if c==1:
    print("BINGO")
print("Largest word length:%d"%(l))
        
              
