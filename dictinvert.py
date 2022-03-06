dict={'hi':1,'hello':6,'happy':6}
inv={v:k for k,v in dict.items()}
print(inv)
k=input("Enter a key:")
if k in dict:
    print("key exists")
