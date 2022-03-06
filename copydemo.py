outf=False
inf=False
try:
   
    outf=open('a.txt','w')
    line=input("Enter text:")
    while line:
        outf.write(line+'\n')
        line=input("Enter texxt:")
except IOError as io:
    print(io)
finally:
    if outf:
        outf.close()
outf=False
try:
    inf=open('a.txt')
    outf=open('new1.txt','a')
    line=inf.read()
    outf.write(line)
except IOError as io:
    print(io)
finally:
    if outf:
        outf.close()
    if inf:
        inf.close()
inf=False
try:
    inf=open('new1.txt')
    print(inf.read())
except IOError as io:
    print(io)
finally:
    if inf:
        inf.close()    
    
