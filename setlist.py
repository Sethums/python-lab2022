l1=list(map(int,input("Enter list1:").split()))
l2=list(map(int,input("Enter list2:").split()))
s1=set(l1)
s2=set(l2)
le=len(s1)
le2=len(s2)
if le==le2:
    print("lengt same")
if sum(s1)==sum(s2):
    print("Sum are same")
if s1.intersection(s2):
    print("Have common ele")
    
