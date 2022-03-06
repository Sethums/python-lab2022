def bin(x):
    if x=='1':
        return x
    else:
        return str(int(x)%2)+bin(str(int(x)//2))
n=input("Enter dec number:")
dec=bin(n)
print(dec[-1::-1])
