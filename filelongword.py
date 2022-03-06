inf=False
try:
    inf=open('abcd.txt')
    w=inf.read().split()
    w.sort(key=len)
   
    
    l=len(w[-1])
    for x in w:
        if len(x)==l:
            print(x)
except IOError as io:
    print(io)
finally:
    if inf:
        inf.close()
