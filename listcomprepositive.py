l=input('Enter integers with spaces:')
l=list(map(int,l.split()))
pos=[x for x in l if x>=0]
print(pos)
print("Length of list:%d"%(len(pos)))
