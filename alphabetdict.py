w=input("Enter word:").lower()
c={}
for i in w:
    c[i]=c.get(i,0)+1
print("Count of each alphabets:\n",c)
