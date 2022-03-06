s=input("Enter a string:")
if len(s)==2:
    print(s+s)
elif len(s)<2:
    print(" ")
else:
    print(s[0:2]+s[len(s)-2:])
    
