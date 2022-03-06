print(list(map(lambda x:int(x)+int(x)*0.1 if int(x)>1000 else int(x)+int(x)*0.05,input("Enter list:").split())))
