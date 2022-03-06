inf=False
outf=False
try:
    inf=open('abcd.txt')
    outf=open('demo.txt','a')
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
    inf=open('demo.txt')
    print(inf.read())
except IOError as io:
    print(io)
finally:
    if inf:
        inf.close()    
